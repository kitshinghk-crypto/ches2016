#!/usr/bin/python3
import numpy as np
from cpa import CPA

traces_file="traces_capdir82/knownrand_fixed/knownrand_fixed_P82_data/traces/2016.06.15-10.13.28_traces.preprocessed.npy"
key_file="traces_capdir82/knownrand_fixed/knownrand_fixed_P82_data/traces/2016.06.15-10.13.28_keylist.npy"
plaintext_file="traces_capdir82/knownrand_fixed/knownrand_fixed_P82_data/traces/2016.06.15-10.13.28_textin.npy"
traces=np.load(traces_file)
key=np.load(key_file)
plaintext=np.load(plaintext_file)

cpa=CPA(traces, key, plaintext)
cpa.train()
cpa.save_train("krf_cpa_corr.npy")
cpa.plot_train("result/knownrand_fixed")


test_traces_file="traces_capdir82/knownfixed_rand/knownfixed_rand_P82_data/traces/2016.06.15-10.09.47_traces.preprocessed.npy"
test_plaintext_file="traces_capdir82/knownfixed_rand/knownfixed_rand_P82_data/traces/2016.06.15-10.09.47_textin.npy"
test_traces=np.load(test_traces_file)
test_plaintext=np.load(test_plaintext_file)
cpa.test(test_traces, test_plaintext)