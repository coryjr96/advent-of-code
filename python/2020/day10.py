from collections import Counter

with open("day10input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n")]
    data = []
    for line in preinput:
        data.append(int(line))

def part1():
    jolts = {1: 0, 2: 0, 3: 0}
    rating = 0
    while True:
        if rating + 1 in data:
            rating = rating + 1
            jolts[1] += 1
        elif rating + 2 in data:
            rating = rating + 2
            jolts[2] += 1
        elif rating + 3 in data:
            rating = rating + 3
            jolts[3] += 1
        else:
            data.append(rating + 3)
            jolts[3] += 1
            return(jolts[3] * jolts[1])

def part2():
    data.sort()
    data.append(data[-1] + 3)
    counter = {0: 1}
    for adapter in data:
        counter[adapter] = counter.get(adapter - 3, 0) + counter.get(adapter - 2, 0) + counter.get(adapter - 1, 0)
    return(counter[data[-1]])


print("Part One Answer:", part1())
print("Part Two Answer:", part2())