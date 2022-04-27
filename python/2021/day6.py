with open("C:\Scripts\Python\Advent of Code\day6input.txt") as fin:
    initfishes = [int(i) for i in fin.read().split(',')]

def part1():
    fishes = initfishes
    day = 0
    while day < 80:
        for a in range(0, len(fishes)):
            if fishes[a] == 0:
                fishes[a] = 6
                fishes.append(8)
            else:
                fishes[a] = fishes[a] - 1
        day += 1
        print(len(fishes))
    return len(fishes)

def part2():
    fishes = initfishes
    day = 0
    while day < 256:
        for a in range(0, len(fishes)):
            if fishes[a] == 0:
                fishes[a] = 6
                fishes.append(8)
            else:
                fishes[a] = fishes[a] - 1
        day += 1
    return len(fishes)

print(part1())