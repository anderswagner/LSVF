import matplotlib.pyplot as plt
from BinaryPoint import *
from LSVF import *
import matplotlib.ticker as mticker

if __name__ == "__main__":
    binaryPoints = []

    repetitions = 5000
    bucketExponents = [2, 4, 8]
    bucketSizes = [2**x for x in bucketExponents]

    collisionsInBucket = [[0] * 1024 for _ in bucketSizes]

    for i in range(1025):
        x = "0" * (1024-i)
        x += "1" * i
        binaryPoints.append(BinaryPoint().fromInt(int(x,2)))

    baselinePoint = binaryPoints[0]

    # The index is now how many bits are set in the binary vector
    # print(binaryPoints[512].hamDistPopCnt(binaryPoints[513]))
    #collisions = [[] for _ in range(1024)]

    for i in range(len(bucketSizes)):
        for _ in range(repetitions):
            lsh = LSVF(binaryPoints, bucketSizes[i], 1, 1024)
            for bucketKey in lsh.buckets[0]:
                if baselinePoint in lsh.buckets[0][bucketKey]:
                    # Do collisions on length
                    for point in lsh.buckets[0][bucketKey]:
                        collisionsInBucket[i][baselinePoint.hamDistPopCnt(point)] += 1
    
    i = 0
    for collisionBucket in collisionsInBucket:
        collisionBucket = [x / repetitions for x in collisionBucket]
        plt.plot(collisionBucket, label=f'k = {bucketExponents[i]}')
        i += 1

    plt.xlabel("Hamming Distance")
    plt.ylabel("Collision Probability (Logarithmic)")
    plt.title("Collision probability for LSVF ")

    plt.yscale("log")
    plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.2f'))

    plt.legend(title="Legend")

    plt.show()