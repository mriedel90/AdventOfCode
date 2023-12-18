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
    return {'id': id, 'winningNumbers': winningNumbers, 'cardNumbers': cardNumbers, 'points': points}

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




file = 'inputs/day4.txt'
sumPoints = SumPoints(file)

print('Sum of Points: ' + str(sumPoints))



# part 1
# sample: Sum of Points: 13
# input: Sum of Points: 23235