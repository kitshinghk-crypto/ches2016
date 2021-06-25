#!/usr/bin/python3
import numpy as np
from aes.aes import AES
import matplotlib.pyplot as plt
from pathlib import Path

class CPA:
    def __init__(self, traces, key, plaintext):
        self.traces = traces
        self.key = key
        self.plaintext = plaintext
        self.key_len = 16
        trace_len = self.traces.shape[1]
        self.corr=np.zeros(shape=(self.key_len,trace_len))
        self.poi = np.zeros(self.key_len, dtype=int)

    def hw(self,n):
        c = 0
        while n:
            c += 1
            n &= n - 1
        return c

    def train(self):
        trace_len = self.traces.shape[1]
        trace_num = self.traces.shape[0]
        state_hw=np.zeros(shape=(trace_num, self.key_len))
        ##Compute output of first subBytes
        for i in range(0, trace_num):
            pt_byte = bytes.fromhex("".join([hex(j)[2:].zfill(2) for j in self.plaintext[i]]))
            key_byte = bytes.fromhex("".join([hex(j)[2:].zfill(2) for j in self.key[i]]))
            aes = AES(key_byte)
            state = aes.first_sub_bytes_state(pt_byte)
            state_hw[i] = [self.hw(s) for s in np.array(state).flatten()]
        ##Compute Pearson Correlation between the power consumption and the hamming weight of the subbyte output for each point in the trace
        for byte_num in range(0, self.key_len):
            for i in range(0,trace_len):
                c = np.corrcoef(self.traces[:,i], state_hw[:,byte_num])
                self.corr[byte_num][i]=c[0][1]
        ##Compute poi
        for i in range(0, self.key_len):
        	self.poi[i] = np.where(abs(self.corr[i])==abs(self.corr[i]).max())[0][0]
    
    def save_train(self, save_file):
        np.save(save_file, self.corr)

    def plot_train(self, save_folder):
        for byte_num in range(0, self.key_len):
            plt.clf()
            plt.plot(self.corr[byte_num])
            folder_path="./"+save_folder
            Path(folder_path).mkdir(parents=True, exist_ok=True)
            plt.savefig(folder_path+"/"+str(byte_num)+".png")

    def test(self, test_traces, test_plaintext):
        trace_num = test_traces.shape[0]
        keyguess=""
        for byte_num in range(0,16):
            max_corr=0
            max_corr_key_byte=0;
            for key_byte in range(0,256):
                key = "0"*32
                i   = byte_num*2
                key = key[:i] + hex(key_byte)[2:].zfill(2) + key[i+2:]
                state_hw = np.zeros(trace_num, dtype=int)
                aes = AES(bytes.fromhex(key))
                for j in range(0, trace_num):
                    pt = bytes.fromhex("".join([hex(pt_b)[2:].zfill(2) for pt_b in test_plaintext[j]]))
                    state = aes.first_sub_bytes_state(pt)
                    hw = [self.hw(s) for s in np.array(state).flatten()]
                    state_hw[j] = hw[byte_num]
                corr = np.corrcoef(test_traces[:, self.poi[byte_num]], state_hw)
                corr = abs(corr[0][1])
                if (corr>max_corr):
                    max_corr = corr
                    max_corr_key_byte = key_byte
            print("byte_num=%d, best_key_byte=%s, corr=%.2f"%(byte_num, hex(max_corr_key_byte)[2:], max_corr))
            keyguess = keyguess + hex(max_corr_key_byte)[2:].zfill(2)
        return keyguess











