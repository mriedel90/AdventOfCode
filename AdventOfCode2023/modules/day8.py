from helpers import *

def ParseDirections(lines):
    return lines[0]

def ParseNode(line):
    element = line[0:3]
    left = line[7:10]
    right = line[12:15]
    return (element, {'L': left, 'R': right})


def ParseNetwork(lines):
    # network is a dictionary, where the key is the element, and value is a dictionary of L and R
    nodes = list(map(ParseNode, lines[2:]))
    network = {element: paths for element, paths in nodes}
    return network
    
def NavigateNetwork(directions, network):
    currentElement = 'AAA'
    destinationElement = 'ZZZ'
    steps = 0
    while currentElement != destinationElement:
        for direction in directions:
            currentElement = network[currentElement][direction]
            steps += 1
            if currentElement == destinationElement:
                return steps


def Part1(file):
    lines = readFileAsLines(file)
    directions = ParseDirections(lines)
    network = ParseNetwork(lines)
    steps = NavigateNetwork(directions, network)
    return steps


def Part2(file):
    lines = readFileAsLines(file)
    return 0





####################

day = get_day(__file__)

# Part 1 Sample Answer: sample: 2, sample2: 6
part1SampleResult = Part1(day + '/sample.txt')
log('Part 1 Sample: ' + str(part1SampleResult))
part1Sample2Result = Part1(day + '/sample2.txt')
log('Part 1 Sample2: ' + str(part1Sample2Result))
part1Result = Part1(day + '/input.txt')
log('Part 1: ' + str(part1Result))


# Part 2 Sample Answer: 
part2SampleResult = Part2(day + '/sample.txt')
log('Part 2 Sample: ' + str(part2SampleResult))
part2Result = Part2(day + '/input.txt')
log('Part 2: ' + str(part2Result))

# Output:

# 2023-12-20 11:21:20: day8
# 2023-12-20 11:21:20: Part 1 Sample: 2
# 2023-12-20 11:21:20: Part 1 Sample2: 6
# 2023-12-20 11:21:20: Part 1: 17263
# 2023-12-20 11:21:20: Part 2 Sample: 0
# 2023-12-20 11:21:20: Part 2: 0