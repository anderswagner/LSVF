import h5py
import time
from BinaryPoint import *
from LSH import LSHBitSampling, LSHDist, LSHDistLSF
from ARGS import *
from util import *

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

    print(LSHLSF_TEXT)

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
        lsh = LSHDistLSF(dataPoints, vectorAmount, permutations)
        end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

        # Run queries
        start = time.time()
        results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
        end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

        # Compare LSH with Truth
        #comparison1 = compare(gt, td, results, amountOfNearestNeighbors, False)
        comparison3 = compare(gt, td, results, amountOfNearestNeighbors, True)
        #print(f"Recall correctness: {comparison1}%. {comparison2}")
        print(f"Recall correctness: {comparison3}%")

    # Close
    q.close()
    f.close()
    testFile.close()