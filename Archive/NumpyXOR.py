import h5py
import numpy as np
import time as t
from BinaryPoint import *
from OldBinaryPoint import *

f = h5py.File('./Datasets/laion2B-en-hammingv2-n=100K.h5', 'r')
dataset = f['hamming']

start_t = t.time()
datapoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(dataset)]
print(t.time() - start_t)

start_t = t.time()
oldPoints = [OldBinaryPoint().fromList(x, i) for i, x in enumerate(dataset)]
print(t.time() - start_t)

start_t = t.time()
for i in range(0, 100000, 2):
    hamDist = datapoints[i].hamDistPopCnt(datapoints[i+1])
print(t.time() - start_t)

start_t = t.time()
for i in range(0, 100000, 2):
    hamDist = oldPoints[i].hamDistPopCnt(oldPoints[i+1])
print(t.time() - start_t)

f.close()