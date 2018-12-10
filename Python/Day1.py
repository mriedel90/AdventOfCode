
fequency = 0
inputFile = open("Day1.txt", "r")
for nextFrequency in inputFile.readlines():
    fequency += int(nextFrequency)
inputFile.close()

print('frequency is: ' + str(fequency))