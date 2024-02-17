def compare(truthIndices: dict, truthDists: dict, result: dict, n: int, useDist: bool):
    maxCorrect = n * len(result)
    wrongNeighors = 0
    # Check all our results
    for k in result:
        tIndices = truthIndices[str(k)][:n]
        tDists = truthDists[str(k)][:n]
        resultArray = result[k]
        resultIndices = resultArray[0]
        resultDists = resultArray[1]
        if useDist:
            for i, v in enumerate(resultDists):
                truthDist = tDists[i]
                if v != truthDist:
                    wrongNeighors += 1
        else:
            for v in resultIndices:
                if v not in tIndices:
                    wrongNeighors += 1
    return ((maxCorrect - wrongNeighors) / maxCorrect) * 100