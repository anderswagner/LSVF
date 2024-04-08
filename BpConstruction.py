import h5py
import numpy as np
import time as t
import random
from BinaryPoint import *
from OldBinaryPoint import *

f = h5py.File('./Datasets/laion2B-en-hammingv2-n=100K.h5', 'r')
dataset = f['hamming']

start_t = t.time()
datapoints = [BinaryPoint().fromList(np.random.randint(0, 2**64, size=16, dtype=np.uint64), i) for i in range (0,1000)]
print(t.time() - start_t)

start_t = t.time()
rngPoints = [BinaryPoint().fromInt(random.randint(0, 2**1024)) for i in range (0,1000)]
print(t.time() - start_t)

f.close()