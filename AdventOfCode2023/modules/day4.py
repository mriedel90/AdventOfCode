import os
from helpers import *


def ParseCard(line):
    id = 0
    winningNumbers = []
    cardNumbers = []
    points = 0

    parts = line[len('Card '):].split(':')
    id = int(parts[0])
    numberSets = [record.split() for record in parts[1].split(' | ')]
    winningNumbers = numberSets[0]
    cardNumbers = numberSets[1]
    points = CalcPoints(winningNumbers, cardNumbers)
    cntMatchingNumbers = CalcMatchingNumbers(winningNumbers, cardNumbers)

    return {'id': id, 'winningNumbers': winningNumbers, 'cardNumbers': cardNumbers, 'points': points, 'cntMatchingNumbers': cntMatchingNumbers}

def CalcPoints(winningNumbers, cardNumbers):
    points = 0
    for number in cardNumbers:
        if (number in winningNumbers):
            if points == 0:
                points = 1
            else:
                points += points
    return points

def CalcMatchingNumbers(winningNumbers, cardNumbers):
    matchingNumbers = 0
    for number in cardNumbers:
        if (number in winningNumbers):
            matchingNumbers += 1
    return matchingNumbers


# part 1
def SumPoints(file):
    lines = readFileAsLines(file)
    cards = [ParseCard(line) for line in lines]
    totalPoints = sum(card['points'] for card in cards)
    return totalPoints

# part 2
def CalcNumberOfTotalCards(file):
    lines = readFileAsLines(file)
    cards = [ParseCard(line) for line in lines]
    
    # start with 1 of each card
    cntEachCard = [1] * len(cards)

    for card in cards:
        for i in range(0, card['cntMatchingNumbers']):
            cntEachCard[card['id'] + i] += cntEachCard[card['id'] - 1]

    totalCards = sum(cntEachCard)
    return totalCards




day = os.path.splitext(os.path.basename(__file__))[0]
print(day)

# Part 1 Sample Answer: 4361
part1SampleResult = SumPoints(day + '/sample.txt')
print('Part 1 Sample: ' + str(part1SampleResult))
part1Result = SumPoints(day + '/input.txt')
print('Part 1: ' + str(part1Result))


# Part 1 Sample Answer: 467835
part2SampleResult = CalcNumberOfTotalCards(day + '/sample.txt')
print('Part 2 Sample: ' + str(part2SampleResult))
part2Result = CalcNumberOfTotalCards(day + '/input.txt')
print('Part 2: ' + str(part2Result))

# Output:
# day4
# Part 1 Sample: 13
# Part 1: 23235
# Part 2 Sample: 30
# Part 2: 5920640
