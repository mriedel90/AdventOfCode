from helperMethods import readFileAsInts

def calculateFrequency(frequecyChanges):
    frequency = 0
    for change in frequencyChanges:
        frequency += change
    return frequency

def calculateFirstFrequencyTwice(frequencyChanges):
    frequency = 0
    frequencies = [0]
    while True:
        for change in frequencyChanges:
            frequency += change
            if frequency in frequencies:
                return frequency
            frequencies.append(frequency)



frequencyChanges = [1, -1]
firstFrequencyTwice = calculateFirstFrequencyTwice(frequencyChanges)
print('first frequency twice is: ' + str(firstFrequencyTwice) + ' should be 0')


frequencyChanges = [3, 3, 4, -2, -4]
firstFrequencyTwice = calculateFirstFrequencyTwice(frequencyChanges)
print('first frequency twice is: ' + str(firstFrequencyTwice) + ' should be 10')


frequencyChanges = [-6, 3, 8, 5, -6]
firstFrequencyTwice = calculateFirstFrequencyTwice(frequencyChanges)
print('first frequency twice is: ' + str(firstFrequencyTwice) + ' should be 5')


frequencyChanges = [7, 7, -2, -7, -4]
firstFrequencyTwice = calculateFirstFrequencyTwice(frequencyChanges)
print('first frequency twice is: ' + str(firstFrequencyTwice) + ' should be 14')



# read from file
frequencyChanges = readFileAsInts("Day1.txt")

freq = calculateFrequency(frequencyChanges)
print('frequency is: ' + str(freq))

firstFrequencyTwice = calculateFirstFrequencyTwice(frequencyChanges)
print('first frequency twice is: ' + str(firstFrequencyTwice))
