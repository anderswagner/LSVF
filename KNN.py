import h5py
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from BinaryPoint import *
from ARGS import *
from util import *
from LSHBitSampling import *

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

    amountOfNearestNeighbors = 5
    num_experiments = 20
    queries_per_second = []

    for experiment in range(num_experiments):
        start = time.time()
        randomIndices = np.random.choice(len(queryPoints), 100, replace=False)
        listSize = len(dataPoints)
        resultDistances = []
        resultIndices = []
        for index in randomIndices:
            # check point
            currentPoint = queryPoints[index]
            currentBests = {}
            for j in range(listSize):
                otherPoint = dataPoints[j]
                currentBests[j] = currentPoint.hamDistPopCnt(otherPoint)
            sortedDists = dict(sorted(currentBests.items(), key=lambda item: item[1]))
            resultIndices.append(list(sortedDists.keys())[:amountOfNearestNeighbors])
            resultDistances.append(list(sortedDists.values())[:amountOfNearestNeighbors])

        elapsed_time = (time.time() - start) / 100
        queries_per_second.append(1.0 / elapsed_time)
        print(f"Experiment {experiment + 1} - Elapsed time: {elapsed_time} seconds - Queries per second: {1.0 / elapsed_time}")

    # Calculate statistics
    mean_time = np.mean(queries_per_second)
    median_time = np.median(queries_per_second)
    std_dev_time = np.std(queries_per_second)

    # Save results to a CSV file
    with open('elapsed_times_stats.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Experiment", "Queries Per Second"])
        for i, elapsed_time in enumerate(queries_per_second):
            writer.writerow([i + 1, elapsed_time])
        writer.writerow([])
        writer.writerow(["Mean Queries Per Second", mean_time])
        writer.writerow(["Median Queries Per Second", median_time])
        writer.writerow(["Standard Deviation of Queries Per Second", std_dev_time])

    # Output the calculated statistics
    print(f"Mean Queries Per Second: {mean_time}")
    print(f"Median Queries Per Second: {median_time}")
    print(f"Standard Deviation of Queries Per Second: {std_dev_time}")
