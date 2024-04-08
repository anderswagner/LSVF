import h5py
import time
from BinaryPoint import *
from ARGS import *
from util import *
from LSHBitSampling import *
from LSHDist import *
from LSVF import *

if __name__ == "__main__":
    # Load input
    f = h5py.File(DS_FILENAME, 'r')
    dataset = f['hamming']
    dataPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(dataset)]

    testFile = h5py.File(GT_FILENAME, 'r')
    gt = testFile['truth_indices']
    td = testFile['distances']

    # Load Queries
    start = time.time()
    q = h5py.File(Q_FILENAME, 'r')
    queries = q['hamming']
    queryPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(queries)]
    end = print(f"Elapsed Loading queries time: {time.time() - start} seconds")

    if (LSHBS_ENABLED):
        print(LSHBS_TEXT)

        for i in range(K_START, K_START + K_INC, 1):
            print("############################")
            # Parameters
            vectorAmount = 1 + i
            permutations = P
            amountOfNearestNeighbors = NN
            queryAmount = Q
            print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

            # Prepare dataset Bit Sampling
            start = time.time()
            lsh = LSHBitSampling(dataPoints, vectorAmount, permutations)
            end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

            # Run queries
            start = time.time()
            results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
            end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

            # Compare LSH with Truth
            #comparison1 = compare(gt, td, results, amountOfNearestNeighbors, False)
            comparison2 = compare(gt, td, results, amountOfNearestNeighbors, True)
            #print(f"Recall correctness: {comparison1}%. {comparison2}")
            print(f"Recall correctness: {comparison2}%")

    if (LSHDS_ENABLED):
        print(LSHDS_TEXT)

        for i in range(K_START, K_START + K_INC, 1):
            print("############################")
            # Parameters
            vectorAmount = 1 + i
            permutations = P
            amountOfNearestNeighbors = NN
            queryAmount = Q
            print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

            # Prepare dataset Bit Sampling
            start = time.time()
            lsh = LSHDist(dataPoints, vectorAmount, permutations)
            end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

            # Run queries
            start = time.time()
            results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
            end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

            # Compare LSH with Truth
            #comparison1 = compare(gt, td, results, amountOfNearestNeighbors, False)
            comparison2 = compare(gt, td, results, amountOfNearestNeighbors, True)
            #print(f"Recall correctness: {comparison1}%. {comparison2}")
            print(f"Recall correctness: {comparison2}%")

    if (LSVF_ENABLED):
        print(LSVF_TEXT)

        for i in range(K_START, K_START + K_INC, 1):
            print("############################")
            # Parameters
            vectorAmount = 1 + i
            permutations = P
            amountOfNearestNeighbors = NN
            queryAmount = Q
            print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

            # Prepare dataset Bit Sampling
            start = time.time()
            lsh = LSVF(dataPoints, vectorAmount, permutations, FILTER_REMOVAL_DISTANCE)
            end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

            # Run queries
            start = time.time()
            results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
            end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

            print(f"Build time stats; Total generate hashes: {lsh.TotalBuildBuckets} | Total hash dataset: {lsh.TotalFindBestDataBucket} | Total append to bucket: {lsh.TotalAppendToBucket}")

            print(f"Query time stats; Total hash and search for best bucket: {lsh.totalSearchForBucket} | Total search in buckets: {lsh.totalSearchInBucket} | Add Points: {lsh.totalAddSearchPoints} | Total rerank result: {lsh.totalReRankPoints}")

            # Compare LSH with Truth
            #comparison1 = compare(gt, td, results, amountOfNearestNeighbors, False)
            comparison3 = compare(gt, td, results, amountOfNearestNeighbors, True)
            #print(f"Recall correctness: {comparison1}%. {comparison2}")
            print(f"Recall correctness: {comparison3}%")

    # Close
    q.close()
    f.close()
    testFile.close()