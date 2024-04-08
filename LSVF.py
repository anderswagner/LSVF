import numpy as np
import random
import time
from BinaryPoint import *

class LSVF:
    def __init__(self, points: list, k: int, p: int):
        self.name = "Distance Points"
        self.points = points
        self.buckets = [[]] * p
        self.k = k
        self.p = p
        self.TotalBuildBuckets = 0.0
        self.TotalFindBestDataBucket = 0.0
        self.TotalAppendToBucket = 0.0
        # p being the amount of permutation "layers"
        for i in range(p):
            self.buckets[i] = {}
            # tmpStart = time.time()
            for indexer in range(2**k):
                # generate a random vector for the given bucket
                x = BinaryPoint().fromList(np.random.randint(0, 2**64, size=16, dtype=np.uint64), indexer) 
                # random.randint(0, 2**1024)

                self.buckets[i][x] = []
            # self.TotalBuildBuckets += (time.time() - tmpStart)
            for point in points:
                # tmpStart = time.time()
                bestDist = 1024
                bestIndex = 0
                # determine which bucket to put it in
                for item in self.buckets[i].keys():
                    dist = point.hamDistPopCnt(item)
                    if dist < bestDist:
                        bestIndex = item
                        bestDist = dist
                # self.TotalFindBestDataBucket += (time.time() - tmpStart)
                # tmpStart = time.time()
                self.buckets[i][bestIndex].append(point)
                # self.TotalAppendToBucket += (time.time() - tmpStart)

    def query(self, queryPoints: list, n: int):
        result = {}
        searchablePoints = set()
        self.totalSearchForBucket = 0.0
        self.totalSearchInBucket = 0.0
        self.totalAddSearchPoints = 0.0
        self.totalReRankPoints = 0.0
        for qp in queryPoints:
            tmpDists = [2**1024] * n
            tmpIndices = [-1] * n
            worstDist = 1024
            # for every permutation of buckets
            for pb in self.buckets:
                # a bucket key is the point i need to compare to
                # tmpStart = time.time()
                bestKey = 0
                bestDist = 1024
                bucketKeys = pb.keys()
                # check all buckets for the best matching bucket for our queryPoint
                for k in bucketKeys:
                    dist = qp.hamDistPopCnt(k)
                    if dist < bestDist:
                        bestKey = k
                        bestDist = dist
                # self.totalSearchForBucket += (time.time() - tmpStart)
                # go through the bucket, add all points to searchable set
                # tmpStart = time.time()
                for bp in pb[bestKey]:
                    searchablePoints.add(bp)
                # self.totalAddSearchPoints += (time.time() - tmpStart)
            # tmpStart = time.time()
            for bp in searchablePoints:
                dist = qp.hamDistPopCnt(bp)
                    # if the distance is better than our worst, see where to put the point
                # tmpStart2 = time.time()
                if dist < worstDist:
                    for i, d in enumerate(tmpDists):
                        if dist < d:
                            # put distance
                            tmpDists[i:] = dist, *tmpDists[i:-1]
                            # put index
                            tmpIndices[i:] = bp.i, *tmpIndices[i:-1]
                            worstDist = tmpDists[-1]
                            # self.totalReRankPoints += (time.time() - tmpStart2)
                            break
            result[qp.i] = (tmpIndices, tmpDists)
            # self.totalSearchInBucket += (time.time() - tmpStart)
        return result

    def queryRandom(self, queryPoints: list, n: int, amount: int):
        pointsToCheck = []
        randomIndices = np.random.choice(len(queryPoints), amount, replace=False)
        for index in randomIndices:
            pointsToCheck.append(queryPoints[index])
        return self.query(pointsToCheck, n)
