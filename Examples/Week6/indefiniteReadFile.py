# when you call readFile you will need to pass in the full path to your file.
# if on Windows, remember to escape your backslashes \
def readFile(filename):
    datafile = open(filename, "r")

    datadict = {}

    key = 0
    aline = datafile.readline ()
    while aline != "":
       key = key + 1
       score = int(aline)
       datadict[key] = [score]

       aline = datafile.readline ()

    return datadict
