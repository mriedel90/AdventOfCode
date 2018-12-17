from helperMethods import readFile

def countOverlappingSpacesSLOW(inputs):
    points = []
    overlappingPoints = []
    for input in inputs:
        startx = int(input.split('@ ')[1].split(',')[0])
        starty = int(input.split('@ ')[1].split(',')[1].split(':')[0])
        right = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[0])
        down = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[1])
        for i in range(0, right):
            for j in range(0, down):
                point = (startx+i, starty+j)
                if point in points and point not in overlappingPoints:
                    overlappingPoints.append(point)
                points.append(point)
    return len(overlappingPoints)

def countOverlappingSpaces(inputs):
    grid = []
    for x in range(0, 1000): 
        grid.append([])
        for y in range(0, 1000):
            grid[x].append([])
    overlappingPoints = 0
    for input in inputs:
        id = int(input.split('#')[1].split(' @')[0])
        startx = int(input.split('@ ')[1].split(',')[0])
        starty = int(input.split('@ ')[1].split(',')[1].split(':')[0])
        right = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[0])
        down = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[1])
        for i in range(0, right):
            for j in range(0, down):
                if len(grid[startx+i][starty+j]) == 1:
                    overlappingPoints = overlappingPoints + 1
                grid[startx+i][starty+j].append(id)
    return overlappingPoints

def getIdForNonOverlapping(inputs):
    grid = []
    for x in range(0, 1000): 
        grid.append([])
        for y in range(0, 1000):
            grid[x].append([])
    overlappingPoints = 0
    for input in inputs:
        id = int(input.split('#')[1].split(' @')[0])
        startx = int(input.split('@ ')[1].split(',')[0])
        starty = int(input.split('@ ')[1].split(',')[1].split(':')[0])
        right = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[0])
        down = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[1])
        for i in range(0, right):
            for j in range(0, down):
                grid[startx+i][starty+j].append(id)
                
    for input in inputs:
        id = int(input.split('#')[1].split(' @')[0])
        startx = int(input.split('@ ')[1].split(',')[0])
        starty = int(input.split('@ ')[1].split(',')[1].split(':')[0])
        right = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[0])
        down = int(input.split('@ ')[1].split(',')[1].split(': ')[1].split('x')[1])
        anyOverlapping = False
        for i in range(0, right):
            for j in range(0, down):
                if len(grid[startx+i][starty+j]) > 1:
                    anyOverlapping = True
                    break
            if anyOverlapping:
                break
        if anyOverlapping == False:
            return id
    return -1



inputs = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
count = countOverlappingSpaces(inputs)
print(count) #4

idOfNonOverlapping = getIdForNonOverlapping(inputs)
print(idOfNonOverlapping) #3

inputs = readFile("Day3.txt")
count = countOverlappingSpaces(inputs)
print(count) #120408

idOfNonOverlapping = getIdForNonOverlapping(inputs)
print(idOfNonOverlapping) #1276