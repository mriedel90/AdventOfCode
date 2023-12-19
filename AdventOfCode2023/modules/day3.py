from helpers import *

def isSpecialChar(x):
    return x != '.' and not x.isdigit()

def GetParts(lines):
    parts = []
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

                # check if the current number is a valid part number, check full circle around digit
                isFirstRow = row == 0
                isLastRow = row == maxRow - 1
                isFirstCol = col == 0
                isLastCol = col == maxCol - 1
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

                # check if this is the end of the number and valid part, add it to parts list
                nextCell = '' if isLastCol else lines[row][col+1]
                if (not nextCell.isdigit() and isCurrentNumberValidPart):
                    parts.append({'partNumber': int(currentNumber), 
                                  'startCol': col-len(currentNumber)+1,
                                  'endCol': col,
                                  'row': row})
                    
                # reset counters
                if (not nextCell.isdigit()):
                    currentNumber = ''
                    isCurrentNumberValidPart = False
    return parts

def GetGears(lines, parts):
    gears = []
    maxRow = len(lines)
    maxCol = len(lines[0]) #logic assumes all lines are the same length (input file is 140x140)
    
    for row in range(maxRow):
        for col in range(maxCol):
            currentCell = lines[row][col]
            if (currentCell == '*'):
                part1 = -1
                part2 = -1
                isGear = False



                for part in parts:
                    
                    
                    if (row == 26 and col == 124 and part['row'] >= row-1 and part['row'] <= row+1):
                        debug = 1
                    
                    
                    # check if part is within 1 row and 1 col from current cell
                    if ((part['row'] >= row-1 and part['row'] <= row+1) and 
                        (part['startCol'] <= col+1 and part['endCol'] >= col-1)):  # not sure about this!
                        if (part1 == -1):
                            part1 = part['partNumber']
                        elif (part2 == -1):
                            part2 = part['partNumber']
                            isGear = True
                        else:
                             isGear = False #more than 2 parts touching gear, makes it invalid
                
                # Check if valid gear, add to collection
                if (isGear):
                    gears.append({'part1': part1, 
                                'part2': part2,
                                'gearRow': row,
                                'gearCol': col})
    return gears


#part 1
def SumParts(file):
    lines = readFileAsLines(file)
    parts = GetParts(lines)
    return sum(part['partNumber'] for part in parts)

#part 2
def SumGearRatios(file):
    lines = readFileAsLines(file)
    parts = GetParts(lines)
    gears = GetGears(lines, parts)
    return sum(gear['part1'] * gear['part2'] for gear in gears)


# Part 1 Sample Answer: 4361
part1SampleResult = SumParts('day3/sample.txt')
print('Part 1 Sample: ' + str(part1SampleResult))
part1Result = SumParts('day3/input.txt')
print('Part 1: ' + str(part1Result))


# Part 1 Sample Answer: 467835
part2SampleResult = SumGearRatios('day3/sample.txt')
print('Part 2 Sample: ' + str(part2SampleResult))
part2Result = SumGearRatios('day3/input.txt')
print('Part 2: ' + str(part2Result))

# Output:
# Part 1 Sample: 4361
# Part 1: 556367
# Part 2 Sample: 467835
# Part 2: 89471771