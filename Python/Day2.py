from helperMethods import readFile

def getChecksum(inputs):
    countOf2 = 0
    countOf3 = 0
    for val in inputs:
        wordHas2 = False
        wordHas3 = False
        for c in val:
            if (val.count(c) == 2): wordHas2 = True
            if (val.count(c) == 3): wordHas3 = True
        if wordHas2: 
            countOf2 += 1
        if wordHas3:
            countOf3 += 1
    return countOf2 * countOf3


inputs = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
checkSum = getChecksum(inputs)
print('checksum is: ' + str(checkSum) + ' should be 12')

inputs = readFile("Day2.txt")
checkSum = getChecksum(inputs)
print('checksum is: ' + str(checkSum))