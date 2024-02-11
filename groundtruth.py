import h5py
from BinaryPoint import *

FILENAME = "./Queries/10k-truth-to-100k-data.h5"

def groundTruth(points: list, queryPoints: list, n: int, indiceGroup, distanceGroup):
    querySize = len(queryPoints)
    listSize = len(points)
    for i in range(querySize):
        currentPoint = queryPoints[i]
        currentBests = {}
        for j in range(listSize):
            otherPoint = points[j]
            currentBests[j] = currentPoint.hamDistPopCnt(otherPoint)
        sortedDists = dict(sorted(currentBests.items(), key=lambda item: item[1]))
        resultIndices = list(sortedDists.keys())[:n]
        indiceGroup.create_dataset(str(i), data=resultIndices)
        resultDistances = list(sortedDists.values())[:n]
        distanceGroup.create_dataset(str(i), data=resultDistances)
        print(f"{i/querySize*100}% complete")

if __name__ == "__main__":
    running = False
    while (not running):
        print(f"Are you sure you want to do this (Y/N)? \n This will oerwrite the file {FILENAME}")
        inp = input()
        if (inp == "Y"):
            running = True
        elif (inp == "N"):
            exit()

    f = h5py.File('./Datasets/laion2B-en-hammingv2-n=100K.h5', 'r')
    dataset = f['hamming']
    dataPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(dataset)]

    q = h5py.File('./Queries/public-queries-10k-hammingv2.h5', 'r')
    queries = q['hamming']
    queryPoints = [BinaryPoint().fromList(x, i) for i, x in enumerate(queries)]

    testFile = h5py.File(FILENAME, 'w')
    gtGroup = testFile.create_group('truth_indices')
    distGroup = testFile.create_group('distances')
    groundTruth(dataPoints, queryPoints, 100, gtGroup, distGroup)
    testFile.close()