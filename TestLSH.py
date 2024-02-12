import h5py
import time
from BinaryPoint import *
from LSH import LSHBitSampling, LSH
from ARGS import *

def compare(truthIndices: dict, truthDists: dict, result: dict, n: int):
    maxCorrect = n * len(result)
    wrongNeighors = 0
    # Check all our results
    for k in result:
        tIndices = truthIndices[str(k)][:n]
        # tDists = truthDists[str(k)][:n]
        resultArray = result[k]
        resultIndices = resultArray[0]
        for v in resultIndices:
            if v not in tIndices:
                wrongNeighors += 1

    print(f"Recall correctness: {((maxCorrect - wrongNeighors) / maxCorrect) * 100}%")

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

    for i in range(K_INC):
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
        compare(gt, td, results, amountOfNearestNeighbors)

    print(LSHDS_TEXT)

    for i in range(K_INC):
        print("############################")
        # Parameters
        vectorAmount = 1 + i
        permutations = P
        amountOfNearestNeighbors = NN
        queryAmount = Q
        print(f"NN = {amountOfNearestNeighbors}, qN = {queryAmount}, k = {vectorAmount}, p = {permutations}")

        # Prepare dataset Bit Sampling
        start = time.time()
        lsh = LSH(dataPoints, vectorAmount, permutations)
        end = print(f"Elapsed LSH construction time: {time.time() - start} seconds")

        # Run queries
        start = time.time()
        results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, queryAmount)
        end = print(f"Elapsed LSH query time: {time.time() - start} seconds")

        # Compare LSH with Truth
        compare(gt, td, results, amountOfNearestNeighbors)

    # Close
    q.close()
    f.close()
    testFile.close()