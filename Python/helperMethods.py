
def readFile(fileName):
    values = []
    inputFile = open(fileName, "r")
    for line in inputFile.readlines():
        values.append(line)
    inputFile.close()
    return values

def readFileAsInts(fileName):
    values = readFile(fileName)
    intValues = []
    for val in values:
        intValues.append(int(val))
    return intValues
