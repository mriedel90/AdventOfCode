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






file = 'inputs/day4-sample.txt'
sumPoints = SumPoints(file)
numCards = CalcNumberOfTotalCards(file)

print('Sum of Points: ' + str(sumPoints))
print('Num Cards: ' + str(numCards))



# part 1
# sample: Sum of Points: 13
# input: Sum of Points: 23235

#part 2 - sample:
# Sum of Points: 13
# Num Cards: 30

#part 2 - input:

# Sum of Points: 23235
# Num Cards: 5920640