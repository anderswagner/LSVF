import numpy as np
import random
from BinaryPoint import *

class LSHDist:
    def __init__(self, points: list, k: int, p: int):
        self.name = "Distance Points"
        self.points = points
        self.buckets = [[]] * p
        self.k = k
        self.p = p
        # p being the amount of permutation "layers"
        for i in range(p):
            self.buckets[i] = {}
            for _ in range(2**k):
                # generate a random vector for the given bucket
                x = random.randint(0, 2**1024)
                self.buckets[i][x] = []
            for point in points:
                bestDist = 1024
                bestIndex = 0
                # determine which bucket to put it in
                for item in self.buckets[i].keys():
                    rPoint = BinaryPoint().fromInt(item)
                    dist = point.hamDistPopCnt(rPoint)
                    if dist < bestDist:
                        bestIndex = item
                        bestDist = dist
                self.buckets[i][bestIndex].append(point)

    def query(self, queryPoints: list, n: int):
        result = {}
        searchablePoints = set()
        for qp in queryPoints:
            tmpDists = [2**1024] * n
            tmpIndices = [-1] * n
            worstDist = 1024
            # for every permutation of buckets
            for pb in self.buckets:
                # a bucket key is the point i need to compare to
                bucketKeys = pb.keys()
                bestKey = 0
                bestDist = 1024
                # check all buckets for the best matching bucket for our queryPoint
                for k in bucketKeys:
                    kPoint = BinaryPoint().fromInt(k)
                    dist = qp.hamDistPopCnt(kPoint)
                    if dist < bestDist:
                        bestKey = k
                        bestDist = dist
                # go through the bucket, add all points to searchable set
                for bp in pb[bestKey]:
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
