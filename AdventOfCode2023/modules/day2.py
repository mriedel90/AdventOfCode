from helpers import *

def parseGame(input):
    parts = input[len('Game '):].split(':')
    id = int(parts[0])
    rounds = [parseRound(record) for record in parts[1].split(';')]
    return {'id': id, 'rounds': rounds}


def parseRound(record):
    red = 0
    blue = 0
    green = 0
    for grab in record.split(','):
        parts = grab.strip().split(' ')
        number = int(parts[0])
        color = parts[1]
        if color == 'red':
            red = number
        elif color == 'green':
            green = number
        elif color == 'blue':
            blue = number
    return {'red': red, 'green': green, 'blue': blue}


def gameScore(game):
    #return 0 if the game is not valid, return gameId if it is
    for round in game['rounds']:
        if (round['red'] > 12 or 
            round['green'] > 13 or
            round['blue'] > 14):
            return 0
    return game['id']

def gamePower(game):
    red = 0
    blue = 0
    green = 0
    for round in game['rounds']:
        if red < round['red']:
            red = round['red']
        if blue < round['blue']:
            blue = round['blue']
        if green < round['green']:
            green = round['green']
    power = red * blue * green
    return power


# part 1 result: 
# sample: 8
# input: 2348
def SumValidGameIds(file):
    sum = 0

    lines = readFileAsLines(file)
    for line in lines:
        game = parseGame(line)
        sum += gameScore(game)
    return sum


# part 2 results:
# sample: 2286
# input: 76008
def SumPowers(file):
    sum = 0

    lines = readFileAsLines(file)
    for line in lines:
        game = parseGame(line)
        sum += gamePower(game)
    return sum




# Part 1 Sample Answer: 8
part1SampleResult = SumValidGameIds('day2/sample.txt')
print('Part 1 Sample: ' + str(part1SampleResult))
part1Result = SumValidGameIds('day2/input.txt')
print('Part 1: ' + str(part1Result))


# Part 1 Sample Answer: 2286
part2SampleResult = SumPowers('day2/sample.txt')
print('Part 2 Sample: ' + str(part2SampleResult))
part2Result = SumPowers('day2/input.txt')
print('Part 2: ' + str(part2Result))

# Output:
# Part 1 Sample: 8
# Part 1: 2348
# Part 2 Sample: 2286
# Part 2: 76008