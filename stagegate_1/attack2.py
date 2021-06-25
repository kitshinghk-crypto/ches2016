#!/usr/bin/python3
import numpy as np
from cpa import CPA

traces_file="traces_capdir57/knownrand_fixed/knownrand_fixed_P57_data/traces/2016.06.01-09.44.52_traces.npy"
key_file="traces_capdir57/knownrand_fixed/knownrand_fixed_P57_data/traces/2016.06.01-09.44.52_keylist.npy"
plaintext_file="traces_capdir57/knownrand_fixed/knownrand_fixed_P57_data/traces/2016.06.01-09.44.52_textin.npy"
traces=np.load(traces_file)
key=np.load(key_file)
plaintext=np.load(plaintext_file)

cpa=CPA(traces, key, plaintext)
cpa.train()
cpa.save_train("kfr_cpa_corr.npy")
cpa.plot_train("result/knwonfixed_rand")


test_traces_file="traces_capdir57/knownfixed_rand/knownfixed_rand_P57_data/traces/2016.06.01-09.41.16_traces.npy"
test_plaintext_file="traces_capdir57/knownfixed_rand/knownfixed_rand_P57_data/traces/2016.06.01-09.41.16_textin.npy"
test_traces=np.load(test_traces_file)
test_plaintext=np.load(test_plaintext_file)
cpa.test(test_traces, test_plaintext)