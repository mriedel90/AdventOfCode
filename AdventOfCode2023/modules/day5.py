import os
from helpers import *




def ProcessMappings(lines):
    seeds, categories = ParseInput(lines)

    # loop through categories
    # loop through seeds
    # find the right mapping, or default to 1=1
    # find category value for the seed

    for category in categories:
        for seed in seeds:
            seed[category['dest']] = \
                GetMappedValue(category['mappings'], seed[category['source']])

    return seeds

def GetMappedValue(mappings, sourceValue):
    for mapping in mappings:
        if (int(sourceValue) >= mapping['sourceRangeStart'] and 
            int(sourceValue) <= mapping['sourceRangeStart'] + mapping['rangeLength']):
            offset = mapping['destRangeStart'] - mapping['sourceRangeStart']
            return sourceValue + offset
    return sourceValue

def ParseInput(lines):

    seeds = [Seed(x) for x in lines[0][len('seeds: '):].split()]
    currentCategory = None
    categories = []
    for line in lines[1:]:
        if line == '':
            if (currentCategory):
                categories.append(currentCategory)
            currentCategory = None
        elif '-to-' in line:
            currentCategory = ParseCategory(line)
        else:
            currentCategory['mappings'].append(ParseCategoryMapping(line))
    
    # add the last one!
    if (currentCategory):
        categories.append(currentCategory)

    return (seeds, categories)

def ParseCategoryMapping(line):
    parts = line.split()
    return {
        'sourceRangeStart': int(parts[1]),
        'destRangeStart': int(parts[0]),
        'rangeLength': int(parts[2])
    }

def ParseCategory(line):
    return {
        'source': line.split('-to-')[0],
        'dest': line.split('-to-')[1].split()[0],
        'mappings': []
    }

def Seed(seed):
     return { 
        'seed': int(seed),
        'soil': -1,
        'fertilizer': -1,
        'water': -1,
        'light': -1,
        'temperature': -1,
        'humidity': -1,
        'location': -1,
    }

# dest = source + x
# x = dest - source
def Part1(file):
    lines = readFileAsLines(file)
    
    seedMappings = ProcessMappings(lines)
    lowestLocation = min(seedMappings, key=lambda x: x['location'])['location']
    return lowestLocation


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


# # Part 1 Sample Answer: 
# part2SampleResult = Part2(day + '/sample.txt')
# print('Part 2 Sample: ' + str(part2SampleResult))
# part2Result = Part2(day + '/input.txt')
# print('Part 2: ' + str(part2Result))

# Output:

# day5
# Part 1 Sample: 35
# Part 1: 600279879