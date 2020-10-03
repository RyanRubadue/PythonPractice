
def findIndices(inputArray, searchValue):
    indicesArray = []
    for i in range(len(inputArray)):
        if type(inputArray[i]) == list:
            for j in findIndices(inputArray[i] , searchValue):
                indicesArray.append([i] + j)
        elif inputArray[i] == searchValue:
            indicesArray.append([i])
    return indicesArray

inputArray = [[[1,2,3], 2, [1,3]], [1,2,3]]
print(findIndices(inputArray, 2))
