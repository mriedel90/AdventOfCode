from helpers import *
import math

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


def NavigateGhostNetwork(directions, network):
    currentElements = [element for element in network.keys() if element.endswith('A')]
    steps = 0
    while not AllCurrentElementsEndWithZ(currentElements):
        for direction in directions:
            currentElements = [network[currentElement][direction] for currentElement in currentElements]
            steps += 1
            if AllCurrentElementsEndWithZ(currentElements):
                return steps


def CalculateStepsUsingLCM(directions, network):

    # approach is to use LCM - figure out how many steps it takes for each starting element to reach a destination element, then LCM those steps
    # apparently to know to do this, the data is structured in a way that the ending element will take you back to the starting element, essentially going in a loop forever

    startingElements = [element for element in network.keys() if element.endswith('A')]
    stepsForAllStartingNodes = []
    for startingElement in startingElements:
        steps = NavigateNetworkForGivenElementUntilNodeEndingWithZ(startingElement, directions, network)
        stepsForAllStartingNodes.append(steps)

    #LCM all the step counts together:
        # use unpacking to pass all step values to the lcm function as params
    result = math.lcm(*stepsForAllStartingNodes)
    return result
            
def NavigateNetworkForGivenElementUntilNodeEndingWithZ(currentElement, directions, network):
    steps = 0
    while not currentElement.endswith('Z'):
        for direction in directions:
            currentElement = network[currentElement][direction]
            steps += 1
            if currentElement.endswith('Z'):
                return steps





def AllCurrentElementsEndWithZ(currentElements):
    return all(element.endswith('Z') for element in currentElements)

def Part1(file):
    lines = readFileAsLines(file)
    directions = ParseDirections(lines)
    network = ParseNetwork(lines)
    steps = NavigateNetwork(directions, network)
    return steps


def Part2(file):
    lines = readFileAsLines(file)
    directions = ParseDirections(lines)
    network = ParseNetwork(lines)
    
    # below approach is Brute Force, which wont work at this scale
    #steps = NavigateGhostNetwork(directions, network)

    steps = CalculateStepsUsingLCM(directions, network)

    return steps





####################

day = get_day(__file__)

# Part 1 Sample Answer: sample: 2, sample2: 6
part1SampleResult = Part1(day + '/sample.txt')
log('Part 1 Sample: ' + str(part1SampleResult))
part1Sample2Result = Part1(day + '/sample2.txt')
log('Part 1 Sample2: ' + str(part1Sample2Result))
part1Result = Part1(day + '/input.txt')
log('Part 1: ' + str(part1Result))


# Part 2 Sample Answer: 6
part2SampleResult = Part2(day + '/sample3.txt')
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


#part 2 - brute force
# 2023-12-20 11:35:21: day8
# 2023-12-20 11:35:21: Part 1 Sample: 2
# 2023-12-20 11:35:21: Part 1 Sample2: 6
# 2023-12-20 11:35:21: Part 1: 17263
# 2023-12-20 11:35:21: Part 2 Sample: 6

# stopped at 12:18 (43 mins) - ran to 330938532 steps
#using LCM (least common multiple) the answer is 14631604759649
# brute force just wont work, need to do LCM


# part 2 - using LCM
# 2023-12-20 12:39:42: day8
# 2023-12-20 12:39:42: Part 1 Sample: 2
# 2023-12-20 12:39:42: Part 1 Sample2: 6
# 2023-12-20 12:39:42: Part 1: 17263
# 2023-12-20 12:39:46: Part 2 Sample: 6
# 2023-12-20 12:39:46: Part 2: 14631604759649