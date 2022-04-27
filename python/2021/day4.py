#format numbers and bingo cards
from typing import Iterable


with open("C:\Scripts\Python\Advent of Code\day4input.txt") as fin:
    draw, *cards = fin.read().split('\n\n')
    draw = [int(i) for i in draw.split(',')]
    allcards = [[[int(col) for col in row.split()] for row in card.split('\n')] for card in cards]

def markcards(draw, card):
    for row in card:
        for col in range(0, len(row)):
            if row[col] == draw:
                row[col] = "X"

def checkwinner(card):
    winner = False
    for row in card:
        winner = all(elem in ["X"] for elem in row)
        if winner:
            return winner

    for col in range(0, 5):
        winner = all(elem in ["X"] for elem in [row[col] for row in card])
        if winner:
            return winner

    return winner
    
def getscore(card):
    sum = 0
    for row in card:
        for num in row:
            if num != "X":
                sum += num
    return(sum)

def part1():
    cards = allcards
    for number in draw:
        for card in cards:
            markcards(number, card)

            if checkwinner(card):
                return getscore(card) * number

def part2():
    cards = allcards
    for number in draw:
        for card in cards:
            markcards(number, card)
            if checkwinner(card):
                allcards.remove(card)
            if len(allcards) == 1:
                for number in draw:
                    markcards(number, cards[0])
                    if checkwinner(cards[0]):
                        return getscore(cards[0]) * number

print(part1())
print(part2())