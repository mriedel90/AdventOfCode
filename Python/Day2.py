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

def differsByOne(val1, val2):
    differsBy = 0
    index = 0
    for c in val1:
        if index < len(val2) and c != val2[index]:
            differsBy += 1
        index += 1
    return differsBy == 1

def getCommonLetters(val1, val2):
    commonLetters = ''
    index = 0
    for c in val1:
        if index < len(val2) and c == val2[index]:
            commonLetters += c
        index += 1
    return commonLetters


def getCommonLettersOfDifferingByOne(inputs):
    for val1 in inputs:
        for val2 in inputs:
            if differsByOne(val1, val2):
                return getCommonLetters(val1, val2)
    return ''


inputs = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
checkSum = getChecksum(inputs)
print('checksum is: ' + str(checkSum) + ' should be 12')

inputs = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
commonLets = getCommonLettersOfDifferingByOne(inputs)
print('common letters are: ' + commonLets + ' should be fgij')


inputs = readFile("Day2.txt")
checkSum = getChecksum(inputs)
print('checksum is: ' + str(checkSum))

commonLets = getCommonLettersOfDifferingByOne(inputs)
print('common letters are: ' + commonLets)