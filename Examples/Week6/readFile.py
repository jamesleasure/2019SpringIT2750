def readFile(filename):
    datafile = open(filename, "r")
    datadict = {}

    key = 0
    for aline in datafile:
       key = key + 1
       score = int(aline)

       datadict[key] = [score]

    return datadict
