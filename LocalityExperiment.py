import numpy as np
import matplotlib.pyplot as plt
from BinaryPoint import *
from LSVF import *


if __name__ == "__main__":
    binaryPoints = []

    for i in range(1025):
        x = "0" * (1024-i)
        x += "1" * i
        binaryPoints.append(BinaryPoint().fromInt(int(x,2)))

    baselinePoint = binaryPoints[0]

    # The index is now how many bits are set in the binary vector
    # print(binaryPoints[512].hamDistPopCnt(binaryPoints[513]))
    #collisions = [[] for _ in range(1024)]
    plotX = []
    plotY = []

    for _ in range(10):
        for i in range(1, 1024, 1):
            lsh = LSVF(binaryPoints, i, 1, 1024)
            for bucketKey in lsh.buckets[0]:
                if baselinePoint in lsh.buckets[0][bucketKey]:
                    # Do collisions on length
                    for point in lsh.buckets[0][bucketKey]:
                        if point != baselinePoint:
                            #collisions[i].append()
                            plotX.append(i)
                            plotY.append(baselinePoint.hamDistPopCnt(point))
        #print(len(collisions[i]))
        print(_)
    
    coef = np.polyfit(plotX, plotY, 2)
    poly = np.poly1d(coef)

    xCurve = np.linspace(min(plotX), max(plotX), 1024)
    yCurve = poly(xCurve)

    plt.scatter(plotX, plotY, s=1, color='black')
    plt.plot(xCurve, yCurve, color="red")
    plt.title("Collisions based on distance and amount of buckets")
    plt.xlabel("Buckets")
    plt.ylabel("Hamming Distance")
    plt.tight_layout()
    plt.show()