import h5py
import random
import time
from BinaryPoint import *
from ARGS import *
import numpy as np
import matplotlib.pyplot as plt
from util import *

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

class LSH:
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

if __name__ == "__main__":

    # Load input
    f = h5py.File('./Datasets/laion2B-en-hammingv2-n=100K.h5', 'r')
    dataset = f['hamming']
    dataPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(dataset)]

    testFile = h5py.File(GT_FILENAME, 'r')
    gt = testFile['truth_indices']
    td = testFile['distances']

    # Load Queries
    start = time.time()
    q = h5py.File('./Queries/public-queries-10k-hammingv2.h5', 'r')
    queries = q['hamming']
    queryPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(queries)]
    #end = print(f"Elapsed Loading queries time: {time.time() - start} seconds")

    for i in range(25):
        #print("############################")
        # Parameters
        vectorAmount = 1 + i
        permutations = 10;
        amountOfNearestNeighbors = 10
        queryAmount = 1
        #print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

        # Prepare dataset Bit Sampling
        start = time.time()
        lsh = LSH(dataPoints, vectorAmount, permutations)
        #end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

        # Debug
        #print(f"Bucket sizes: ")
        lens = []
        for x in range(permutations):
            for z in lsh.buckets[x]:
                lens.append(len(lsh.buckets[x][z]))
        standardDev = np.std(lens)
        mean = np.mean(lens)
        mini = min(lens)
        maxi = max(lens)

        fig, (ax1, ax2) = plt.subplots(2, 1, gridspec_kw={'height_ratios': [1, 2]}, figsize=(8, 6))

        ax1.hist(lens, bins=10, edgecolor='black')
        ax1.set_title('Histogram')

        bars_stats = ax2.bar(["Min", "Max", "Std Dev", "Mean"], [mini, maxi, standardDev, mean])
        ax2.set_title(f"Stats: k={vectorAmount}, p={permutations}, LSH={lsh.name}")

        for bar, value in zip(bars_stats, [mini, maxi, standardDev, mean]):
            ax2.text(bar.get_x() + bar.get_width() / 2, value, f"{value:.2f}",
                    ha='center', va='bottom')
        plt.tight_layout()
        plt.show()

        # Run queries
        start = time.time()
        results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
        #end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

        # Compare LSH with Truth
        r1 = compare(gt, td, results, amountOfNearestNeighbors, False)
        r2 = compare(gt, td, results, amountOfNearestNeighbors, True)
        print(f"{r1}, {r2}")

    # Close
    q.close()
    f.close()
    testFile.close()