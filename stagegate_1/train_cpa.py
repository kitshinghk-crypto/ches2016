#!/usr/bin/python3
import numpy as np
from aes.aes import AES
import matplotlib.pyplot as plt
from pathlib import Path

def hw(n):
    c = 0
    while n:
        c += 1
        n &= n - 1
    return c


is_plot=True
traces_file="traces_capdir57/knownfixed_rand/knownfixed_rand_P57_data/traces/2016.06.01-09.41.16_traces.npy"
key_file="traces_capdir57/knownfixed_rand/knownfixed_rand_P57_data/traces/2016.06.01-09.41.16_keylist.npy"
plaintext_file="traces_capdir57/knownfixed_rand/knownfixed_rand_P57_data/traces/2016.06.01-09.41.16_textin.npy"

traces=np.load(traces_file)
key=np.load(key_file)
plaintext=np.load(plaintext_file)

trace_len = traces.shape[1]
trace_num = traces.shape[0]
key_len = 16
corr=np.zeros(shape=(key_len,trace_len))
state_hw=np.zeros(shape=(trace_num, key_len))

##Compute output of first subBytes
for i in range(0,trace_num):
	pt_byte = bytes.fromhex("".join([hex(j)[2:].zfill(2) for j in plaintext[i]]))
	key_byte = bytes.fromhex("".join([hex(j)[2:].zfill(2) for j in key[i]]))
	aes = AES(key_byte)
	state = aes.first_sub_bytes_state(pt_byte)
	state_hw[i] = [hw(s) for s in np.array(state).flatten()]

##Compute Pearson Correlation between the power consumption and the hamming weight of the subbyte output for each point in the trace
for byte_num in range(0,key_len):
    for i in range(0,trace_len):
        c = np.corrcoef(traces[:,i], state_hw[:,byte_num])
        corr[byte_num][i]=c[0][1]

if is_plot:
	for byte_num in range(0, key_len):
	    plt.clf()
	    plt.plot(corr[byte_num])
	    folder_path="./cpa_train_result"
	    Path(folder_path).mkdir(parents=True, exist_ok=True)
	    plt.savefig(folder_path+"/"+str(byte_num)+".png")

