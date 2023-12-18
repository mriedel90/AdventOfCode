from helpers import *

def isSpecialChar(x):
    return x != '.' and not x.isdigit()

def SumParts():
    sum = 0

    lines = readFileAsLines('inputs/day3.txt')
    maxRow = len(lines)
    maxCol = len(lines[0]) #logic assumes all lines are the same length (input file is 140x140)
    
    currentNumber = ''
    isCurrentNumberValidPart = False

    for row in range(maxRow):
        for col in range(maxCol):
            currentCell = lines[row][col]
            if (currentCell.isdigit()):
                # build the currentNumber
                currentNumber += currentCell
                
                isFirstRow = row == 0
                isLastRow = row == maxRow - 1
                isFirstCol = col == 0
                isLastCol = col == maxCol - 1

                # check if the current number is a valid part number, check full circle around digit
                if (not isCurrentNumberValidPart and
                        #top left
                        (not isFirstRow and not isFirstCol and isSpecialChar(lines[row-1][col-1])) or
                        #top
                        (not isFirstRow and isSpecialChar(lines[row-1][col])) or 
                        #top right
                        (not isFirstRow and not isLastCol and isSpecialChar(lines[row-1][col+1])) or 
                        #right
                        (not isLastCol and isSpecialChar(lines[row][col+1])) or 
                        #bottom right
                        (not isLastRow and not isLastCol and isSpecialChar(lines[row+1][col+1])) or 
                        #bottom
                        (not isLastRow and isSpecialChar(lines[row+1][col])) or 
                        #bottom left
                        (not isLastRow and not isFirstCol and isSpecialChar(lines[row+1][col-1])) or 
                        #left
                        (not isFirstCol and isSpecialChar(lines[row][col-1]))):
                            isCurrentNumberValidPart = True

                # check if this is the end of the number and valid part, add it to sum
                nextCell = '' if isLastCol else lines[row][col+1]
                if (not nextCell.isdigit() and isCurrentNumberValidPart):
                    sum += int(currentNumber)
                if (not nextCell.isdigit()):
                    currentNumber = ''
                    isCurrentNumberValidPart = False
    return sum


x = SumParts()

print('Sum: ' + str(x))

#sample: Sum: 4361
#input: Sum: 556367