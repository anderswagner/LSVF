import h5py
import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from BinaryPoint import *
from ARGS import *
from util import *
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

    amountOfNearestNeighbors = 5

    recalls = []
    times = []
    recalls_per_second = []
    parameters = []

    for p in range(1, 16, 1):
        for i in range(1, 6, 1):
            for d in range(470, 495, 5):
                start = time.time()
                lsh = LSVF(dataPoints, 2**i, p, d)
                print(f"Constructed {p}, {i}, {d}")

                start = time.time()
                results = lsh.queryRandom(queryPoints, amountOfNearestNeighbors, 100)
                elapsed_time = (time.time() - start) / 100
                recall = compare(gt, td, results, amountOfNearestNeighbors, True)
                if elapsed_time != 0.0 and recall >= 90.0:
                    times.append(elapsed_time)
                    recalls.append(recall)
                    recalls_per_second.append(1.0 / elapsed_time)
                    parameters.append(f"{p},{i},{d}")
                    print(f"Elapsed LSH query time: {elapsed_time} seconds")

    with open('recalls_and_times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Parameters", "Recall (%)", "Time Taken (seconds)", "Recalls per Second"])
        for parameter, recall, time_taken, rps in zip(parameters, recalls, times, recalls_per_second):
            writer.writerow([parameter, recall, time_taken, rps])

    plt.figure(figsize=(10, 6))
    plt.scatter(recalls, recalls_per_second, c='blue')
    plt.title('Recall vs Recalls per Second')
    plt.xlabel('Recall (%)')
    plt.ylabel('Recalls per Second')
    plt.grid(True)
    plt.show()