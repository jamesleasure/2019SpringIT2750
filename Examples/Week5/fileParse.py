fileIn = open("/Users/James/Downloads/access_log.log", "r")
fileOut = open("/Users/James/Downloads/access_log-10.0.0.153.log", "w")

for line in fileIn:
    values = line.split()
    i = 0
    #if len(values) > 6:
    fromAddr = values[0]
    timeStamp = values[3].replace("[", "")
    method = values[5].replace('"', "")
    resource = values[6]
    status = ""
    #if len(values) > 7:
    #    status = values[8]
    if fromAddr == "10.0.0.153":
        fileOut.write(line)
    print(f"address: {fromAddr}")
    print(f"timeStamp: {timeStamp}")
    print(f"method: {method}")
    #print(f"status: {status}")
    print(f"resource: {resource}")
    print()
    i = i + 1
     #break

fileIn.close()
fileOut.close()