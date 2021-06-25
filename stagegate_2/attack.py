#!/usr/bin/python3
import numpy as np
from cpa import CPA

traces_file="traces_capdir58/knownfixed_rand/knownfixed_rand_P58_data/traces/2016.06.01-11.50.56_traces.preprocessed.npy"
key_file="traces_capdir58/knownfixed_rand/knownfixed_rand_P58_data/traces/2016.06.01-11.50.56_keylist.npy"
plaintext_file="traces_capdir58/knownfixed_rand/knownfixed_rand_P58_data/traces/2016.06.01-11.50.56_textin.npy"
traces=np.load(traces_file)
key=np.load(key_file)
plaintext=np.load(plaintext_file)

cpa=CPA(traces, key, plaintext)
cpa.train()
cpa.save_train("kfr_cpa_corr.npy")
cpa.plot_train("result/knwonfixed_rand")


test_traces_file="traces_capdir58/secretfixed_rand/secretfixed_rand_P58_data/traces/2016.06.01-12.00.09_traces.preprocessednpy"
test_plaintext_file="traces_capdir58/secretfixed_rand/secretfixed_rand_P58_data/traces/2016.06.01-12.00.09_textin.npy"
test_traces=np.load(test_traces_file)
test_plaintext=np.load(test_plaintext_file)
print(cpa.test(test_traces, test_plaintext))