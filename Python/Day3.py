from helperMethods import readFile

def countOverlappingSpaces(inputs):
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

inputs = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
count = countOverlappingSpaces(inputs)
print(count) #4

inputs = readFile("Day3.txt")
count = countOverlappingSpaces(inputs)
print(count) #120408