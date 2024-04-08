import numpy as np

class BinaryPoint:
    def __init__(self):
        self.arr = np.ndarray(shape=(16,), dtype=np.uint64)

    def fromList(self, inputList: np.ndarray, i: int):
        self.i = i
        self.arr = inputList
        return self

    def fromInt(self, x: int):        
        binary_str = format(x, "01024b")
        chunks = [binary_str[i : i + 64] for i in range(0, 1024, 64)]
        chunk_integers = np.array([int(chunk, 2) for chunk in chunks], dtype=np.uint64)
        self.arr = chunk_integers
        return self

    def hamDistPopCnt(self, other: 'BinaryPoint') -> int:
        return hamDistNP(self.arr, other.arr)
    
    def bitSample(self, bits: list) -> int:
        unpackedView = np.unpackbits(self.arr.view(np.uint8))
        l = len(bits)
        result = []
        for b in bits:
            result.append(unpackedView[b])
        paddedResult = np.pad(result, (0,64-l), 'constant')
        return np.packbits(paddedResult).view(np.uint64)[0]

def hamDistNP(left: np.ndarray, right: np.ndarray) -> int:
    xorCalc = left ^ right
    bits = np.unpackbits(xorCalc.view(np.uint8)).reshape((-1,8))
    return np.sum(np.sum(bits, axis=1))