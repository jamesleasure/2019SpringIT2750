import os 

def railBreak(cipherText):
    currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"
    wordDict = createWordDict(currentPath + 'wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary"
    for i in range (1, cipherLen +1):
        print(i)
        words = railDecrypt(cipherText,i)
        print(words)
        goodCount = 0
        for w in words :
            if w in wordDict:
                goodCount = goodCount + 1
        print(f"goodCount for {i}: {goodCount}")
        if goodCount > maxGoodSoFar :
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words)
    print("Best Guess: " + bestGuess)
    return bestGuess

def railDecrypt(cipherText, numRails):
    railLen = len(cipherText) // numRails
    solution = ''
    for col in range(railLen):
        for rail in range(numRails):
            #print(f"col: {col} rail: {rail} railLen: {railLen}")
            nextLetter = (col + rail * railLen)
            #print(f"nextLetter: {nextLetter}")
            solution = solution + cipherText[nextLetter]
            #print(f"solution: {solution}")
    return solution.split()

def createWordDict(dname):
    myDict = {}
    myFile = open(dname, 'r')
    for line in myFile:
        myDict[line [: -1]] = True
    return myDict


railBreak("n oci mreidontoowp mgorw")
