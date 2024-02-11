class BinaryPoint:
    def __init__(self):
        self.x = 0

    def fromList(self, inputList: list, i: int):
        self.i = i
        tmp = ""
        for y in inputList:
            b = bin(y)[2:]
            b = '0' * (64-len(b)) + b
            tmp += b
        self.x = int(tmp, 2)
        return self

    def fromInt(self, x: int):
        self.x = x
        return self

    def hamDistPopCnt(self, other: 'BinaryPoint') -> int:
        return hamDistPopCount(self.x, other.x)
    
    def bitSample(self, bits: list) -> int:
        bitString = bin(self.x)[2:]
        result = ""
        for b in bits:
            if len(bitString) > b:
                if bitString[b] == '1':
                    result += "1"
                else:
                    result += "0"
            else:
                result += "0"
        return int(result, 2)

    def toIntList(self, bits: int) -> list[int]:
        y = bin(self.x)[2:]
        size = len(y)
        pieces = size//bits
        l = [0] * pieces
        for i in range(pieces):
            p = y[(bits*i):bits*(i+1)]
            l[i] = int(p, 2)
        return l

def hamDistPopCount(a: int, b : int) -> int:
    xor = a ^ b
    return xor.bit_count()