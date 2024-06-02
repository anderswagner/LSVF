import numpy as np
import random
from BinaryPoint import *

x = np.random.randint(0, 2**64, size=16, dtype=np.uint64)

b = BinaryPoint().fromList(x, 0)

y = random.randint(0, 2**1024)

print(x)
print(y)

viewed = x.view(np.uint8)
unpacked = np.unpackbits(viewed)
#print(b.bitSample(np.arange(4)))