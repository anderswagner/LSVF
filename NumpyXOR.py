import h5py
import numpy as np
import time as t
from BinaryPoint import *

f = h5py.File('./Datasets/laion2B-en-hammingv2-n=100K.h5', 'r')
dataset = f['hamming']

start_t = t.time()
for i in range(0, 100000, 2):
    bp_a = BinaryPoint().fromList(dataset[i], 0)
    bp_b = BinaryPoint().fromList(dataset[i+1], 1)
    hamCount = bp_a.hamDistPopCnt(bp_b)
print(t.time() - start_t)

start_t = t.time()
for i in range(0, 100000, 2):
    xor = dataset[i] ^ dataset[i+1]
    bits = np.unpackbits(xor.view(np.uint8)).reshape((-1,8))
    bitCount = np.sum(bits, axis=1)
    hamDist = np.sum(bitCount)
print (t.time() - start_t)

f.close()