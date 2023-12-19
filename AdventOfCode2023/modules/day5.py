import os
from helpers import *



def Part1(file):
    lines = readFileAsLines(file)
    return 0


def Part2(file):
    lines = readFileAsLines(file)
    return 0




####################


day = os.path.splitext(os.path.basename(__file__))[0]
print(day)

# Part 1 Sample Answer: 
part1SampleResult = Part1(day + '/sample.txt')
print('Part 1 Sample: ' + str(part1SampleResult))
part1Result = Part1(day + '/input.txt')
print('Part 1: ' + str(part1Result))


# Part 1 Sample Answer: 
part2SampleResult = Part2(day + '/sample.txt')
print('Part 2 Sample: ' + str(part2SampleResult))
part2Result = Part2(day + '/input.txt')
print('Part 2: ' + str(part2Result))

# Output: