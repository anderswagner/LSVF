import numpy as np
from BinaryPoint import *

class LSHBitSampling:
    def __init__(self, points: list, k: int, p: int):
        self.name = "Bit Sampling"
        self.points = points
        self.buckets = [[]] * p
        self.bitChoices = []
        self.k = k
        self.p = p
        # p being the amount of permutations
        for i in range(p):
            self.buckets[i] = {}
            bitChoice = np.sort(np.random.choice(1024, k, replace=False))
            for x in range(2**k):
                self.buckets[i][x] = []
            self.bitChoices.append(bitChoice)
            for point in points:
                sample = point.bitSample(bitChoice)
                self.buckets[i][sample].append(point)

    def query(self, queryPoints: list, n: int):
        result = {}
        searchablePoints = set()
        for qp in queryPoints:
            tmpDists = [2**1024] * n
            tmpIndices = [-1] * n
            worstDist = 1024
            # for every permutation of buckets
            for i, pb in enumerate(self.buckets):
                sampleKey = self.bitChoices[i]
                sample = qp.bitSample(sampleKey)
                for bp in pb[sample]:
                    searchablePoints.add(bp)
            
            for bp in searchablePoints:
                dist = qp.hamDistPopCnt(bp)
                # if the distance is better than our worst, see where to put the point
                if dist < worstDist:
                    for i, d in enumerate(tmpDists):
                        if dist < d:
                            # put distance
                            tmpDists[i:] = dist, *tmpDists[i:-1]
                            # put index
                            tmpIndices[i:] = bp.i, *tmpIndices[i:-1]
                            worstDist = tmpDists[-1]
                            break
            result[qp.i] = (tmpIndices, tmpDists)
        return result

    def queryRandom(self, queryPoints: list, n: int, amount: int):
        pointsToCheck = []
        randomIndices = np.random.choice(len(queryPoints), amount, replace=False)
        for index in randomIndices:
            pointsToCheck.append(queryPoints[index])
        return self.query(pointsToCheck, n)
