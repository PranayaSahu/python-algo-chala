def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    indexOne = 0
    indexTwo = 0
    smallest = float("inf")
    current = float("inf")
    smallestPair = []

    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        firstNum = arrayOne[indexOne]
        secondNum = arrayTwo[indexTwo]
        current = abs(firstNum - secondNum)

        if current < smallest:
            smallest = current
            smallestPair = [firstNum, secondNum]

        if firstNum < secondNum:
            indexOne += 1
        elif firstNum > secondNum:
            indexTwo += 1
        else:
            return [firstNum , secondNum] 

    return smallestPair

if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17, 28]
    print(smallestDifference(arrayOne, arrayTwo)) 