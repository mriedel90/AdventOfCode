import os
from helpers import *




def ProcessMappings(seeds, categories):

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

def ParseSeedsV1(lines):
    return [Seed(x) for x in lines[0][len('seeds: '):].split()]


def ParseSeedsV2(lines):
    seeds = []
    seedParts = [int(x) for x in lines[0][len('seeds: '):].split()]

    seedStart = -1
    for seedPart in seedParts:
        if seedStart == -1:
            seedStart = seedPart
        else:
            numSeeds = seedPart
            seeds += [Seed(seedStart + i) for i in range(numSeeds)]
            seedStart = -1

    #  iterate through odd numbers until the end of the range 
    # for i in range(len(seedParts))[::2]:
    #     seedStart = seedParts[i]
    #     numSeeds = seedParts[i+1]
    #     seeds += [Seed(seedStart + i) for i in range(numSeeds)]
    return seeds

def ParseCategories(lines):
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

    return categories

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

    seeds = ParseSeedsV1(lines)
    categories = ParseCategories(lines)
    seedMappings = ProcessMappings(seeds, categories)
    lowestLocation = min(seedMappings, key=lambda x: x['location'])['location']
    return lowestLocation


def Part2(file):
    lines = readFileAsLines(file)

    seeds = ParseSeedsV2(lines)
    categories = ParseCategories(lines)
    seedMappings = ProcessMappings(seeds, categories)
    lowestLocation = min(seedMappings, key=lambda x: x['location'])['location']
    return lowestLocation




####################


day = get_day(__file__)

# Part 1 Sample Answer: 35
part1SampleResult = Part1(day + '/sample.txt')
log('Part 1 Sample: ' + str(part1SampleResult))
part1Result = Part1(day + '/input.txt')
log('Part 1: ' + str(part1Result))


# # Part 1 Sample Answer: 46
part2SampleResult = Part2(day + '/sample.txt')
log('Part 2 Sample: ' + str(part2SampleResult))
part2Result = Part2(day + '/input.txt')
log('Part 2: ' + str(part2Result))

# Output:

# 2023-12-19 00:52:44: day5
# 2023-12-19 00:52:51: Part 1 Sample: 35
# 2023-12-19 00:52:51: Part 1: 600279879
# 2023-12-19 00:52:57: Part 2 Sample: 46
