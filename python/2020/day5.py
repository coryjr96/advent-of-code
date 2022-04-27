import math

with open("day5input.txt") as fin:
    passes = [i for i in fin.read().strip().split("\n")]

def part1():
    seatids = []
    for pas in passes:
        min = 0
        max = 127
        rmin = 0
        rmax = 7
        for letter in range(0, 7):
            if pas[letter] == "F":
                max = min + ((max - min) // 2)
            if pas[letter] == "B":
                min = min + (math.ceil((max - min) / 2))
            row = max
        for letter in range(7, 10):
            if pas[letter] == "L":
                rmax = rmin + ((rmax - rmin) // 2)
            if pas[letter] == "R":
                rmin = rmin + (math.ceil((rmax - rmin) / 2))
            column = rmax
        seatids.append(int(row * 8 + column))
    return(seatids)

def part2(seatids):
    numbers = []
    for a in range(27, 963):
        numbers.append(a)
    for seat in range(len(seatids)):
        if seatids[seat] in numbers:
            numbers.remove(seatids[seat])
    return(numbers[0])

seatids = part1()
print("Part One Answer:", max(seatids))
myseat = part2(seatids)
print("Part Two Answer:", myseat)