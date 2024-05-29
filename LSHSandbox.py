import h5py
import time
import numpy as np
import matplotlib.pyplot as plt
from ARGS import *
from BinaryPoint import *
from util import *
from LSHBitSampling import *
from LSHDist import *
from LSVF import *

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

    for i in range(4, 5, 1):
        #print("############################")
        # Parameters
        vectorAmount = 1 + i
        permutations = 10;
        amountOfNearestNeighbors = 10
        queryAmount = 100
        distanceThreshold = 485
        #print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

        # Prepare dataset Bit Sampling
        start = time.time()
        lsh = LSVF(dataPoints, 2**vectorAmount, permutations, distanceThreshold)
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