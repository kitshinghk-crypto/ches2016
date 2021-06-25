#!/usr/bin/python3
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
ref_traces_file="traces_capdir82/knownfixed_rand/knownfixed_rand_P82_data/traces/2016.06.15-10.09.47_traces.npy"
ref_traces=np.load(ref_traces_file)
ref_subtrace= ref_traces[0][916:930]
#traces_file="traces_capdir82/knownfixed_rand/knownfixed_rand_P82_data/traces/2016.06.15-10.09.47_traces.npy"
#traces_file="traces_capdir82/knownrand_fixed/knownrand_fixed_P82_data/traces/2016.06.15-10.13.28_traces.npy"
traces_file="traces_capdir82/secretfixed_rand/secretfixed_rand_P82_data/traces/2016.06.15-10.19.19_traces.npy"
traces = np.load(traces_file)
traces_num = traces.shape[0]
traces_extract = np.zeros(shape=(traces_num, len(ref_subtrace)*16))
for i in range(0,traces_num):
    c=np.correlate(traces[i][200:], ref_subtrace, "full")
    peaks, _ = find_peaks(c, height=0.015, distance=len(ref_subtrace))
    peaks = peaks[:16] + 200
    #plt.plot(traces[i])
    #plt.plot(peaks, traces[i][peaks],"x")
    #plt.show()
    te = np.zeros(0);
    for j in range(0,16):
        te = np.concatenate((te, traces[i][peaks[j]-len(ref_subtrace)+1:peaks[j]+1]),axis=None)
    #plt.plot(te)
    #plt.show()
    traces_extract[i] = te
#np.save("traces_capdir82/knownfixed_rand/knownfixed_rand_P82_data/traces/2016.06.15-10.09.47_traces.extract.npy", traces_extract)
#np.save("traces_capdir82/knownrand_fixed/knownrand_fixed_P82_data/traces/2016.06.15-10.13.28_traces.extract.npy", traces_extract)
np.save("traces_capdir82/secretfixed_rand/secretfixed_rand_P82_data/traces/2016.06.15-10.19.19_traces.extract.npy",traces_extract)