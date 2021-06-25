#!/usr/bin/python3
import numpy as np
#traces_file="traces_capdir58/knownfixed_rand/knownfixed_rand_P58_data/traces/2016.06.01-11.50.56_traces.npy"
traces_file="traces_capdir58/knownrand_fixed/knownrand_fixed_P58_data/traces/2016.06.01-11.54.29_traces.npy"
traces = np.load(traces_file)
traces_num = traces.shape[0]
traces_offset= np.zeros(traces_num,dtype=int)
ref_trace = traces[0]
for i in range(0,traces_num):
	corr = np.correlate(ref_trace, traces[i], "full");
	offset = np.where(corr==corr.max())[0][0]
	traces_offset[i] = offset + 1
traces_offset = traces_offset - traces.shape[1]
min_offset = traces_offset.min()
for i in range(0,traces_num):
	traces[i] = np.roll(traces[i], -(traces_offset[i]-min_offset))
#np.save("traces_capdir58/knownfixed_rand/knownfixed_rand_P58_data/traces/2016.06.01-11.50.56_traces.preprocessed.npy", traces)
np.save("traces_capdir58/knownrand_fixed/knownrand_fixed_P58_data/traces/2016.06.01-11.54.29_traces.preprocessed.npy", traces)