
import sys

# result: 55093
# result: 54249
def SumCalibrationValuesV2(file):
    sum = 0
    lines = getLines(file)
    for line in lines:
        cv = CalibrationValueV2(line)
        sum += cv
    return sum



# result: 55002
# result: 53194
def SumCalibrationValues(file):
    sum = 0
    lines = getLines(file)
    for line in lines:
        cv = CalibrationValue(line)
        sum += cv
    return sum



def CalibrationValueV2(input):
    # combine first digit and last digit
    # to create a 2 digit integer
    firstDigit = ''
    lastDigit = ''
    for char in input:
        if char.isdigit():
            firstDigit = char
            break
    for char in reversed(input):
        if char.isdigit():
            lastDigit = char
            break
    
    firstDigitIndex = len(input) + 1 if firstDigit == '' else input.find(firstDigit)
    lastDigitIndex = -1 if lastDigit == '' else input.rfind(lastDigit)

    numbers_and_words = [
    (1, "one"),
    (2, "two"),
    (3, "three"),
    (4, "four"),
    (5, "five"),
    (6, "six"),
    (7, "seven"),
    (8, "eight"),
    (9, "nine")
    ]

    for number, word in numbers_and_words:
        firstWordIndex = input.find(word)
        if (firstDigitIndex > firstWordIndex & firstWordIndex >= 0):
            firstDigit = number
            firstDigitIndex = firstWordIndex
        lastWordIndex = input.rfind(word)
        if (lastDigitIndex < lastWordIndex & lastWordIndex >= 0):
            lastDigit = number
            lastDigitIndex = lastWordIndex

    value = str(firstDigit) + str(lastDigit)
    return int(value)

def CalibrationValue(input):
    # combine first digit and last digit
    # to create a 2 digit integer
    for char in input:
        if char.isdigit():
            x1 = char
            break
    for char in reversed(input):
        if char.isdigit():
            x2 = char
            break

    
    

    return int(x1 + x2)


def getLines(filePath):
    lines = []
    with open(filePath) as file:
        for line in file.readlines():
            lines.append(line.strip())
    return lines


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


class Day1:

    def CalibrationValue(self, input):
        # combine first digit and last digit
        # to create a 2 digit integer
        x1, x2 = 0
        for char in input:
            if char.isdigit():
                x1 = char
        for char in reversed(input):
            if char.isdigit():
                x2 = char
        return int(x1 + x2)
    




    def CompareReversedSlice(self):

        my_list = list(range(1000000))

        # Using reversed()
        for item in reversed(my_list):
            pass

        # Using slicing
        for item in my_list[::-1]:
            pass

        # Compare memory usage
        print(sys.getsizeof(reversed(my_list)))  # 48 = Less memory usage
        print(sys.getsizeof(my_list[::-1]))      # 8000056 = More memory usage



# Part 1 Sample Answer: 142
part1SampleResult = SumCalibrationValues('day1/sample.txt')
print('Part 1 Sample: ' + str(part1SampleResult))
part1Result = SumCalibrationValues('day1/input.txt')
print('Part 1: ' + str(part1Result))


# Part 1 Sample Answer: 281
part2SampleResult = SumCalibrationValuesV2('day1/sample2.txt')
print('Part 2 Sample: ' + str(part2SampleResult))
part2Result = SumCalibrationValuesV2('day1/input.txt')
print('Part 2: ' + str(part2Result))

# Output:
# Part 1 Sample: 142
# Part 1: 53194
# Part 2 Sample: 281
# Part 2: 54249
