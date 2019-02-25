import os 

currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"

def railBreak(cipherText):
    currentPath = os.path.dirname(os.path.realpath(__file__)) + "/"
    wordDict = createWordDict(currentPath + 'wordlist.txt')
    cipherLen = len(cipherText)
    maxGoodSoFar = 0
    bestGuess = "No words found in dictionary"
    for i in range (1, cipherLen +1):
        words = railDecrypt(cipherText,i)
        goodCount = 0
        for w in words :
            if w in wordDict:
                goodCount = goodCount + 1
        if goodCount > maxGoodSoFar :
            maxGoodSoFar = goodCount
            bestGuess = " ".join(words)
    return bestGuess

def createWordDict(dname):
    myDict = {}
    myFile = open(dname, 'r')
    for line in myFile:
        myDict[line [: -1]] = True
    return myDict

