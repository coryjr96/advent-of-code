with open("day9input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n")]
    data = []
    preamble = []
    for line in preinput:
        data.append(int(line))
    for i in range(25):
        preamble.append(data[i])

def part1():
    def sumfinder(preamble):
        sums = []
        for x in preamble:
            for y in preamble:
                if x != y:
                    sums.append(x + y)
        return(sums)
    for i in range(25, 1000):
        sums = sumfinder(preamble)
        if data[i] in sums:
            preamble.remove(data[(i - 25)])
            preamble.append(data[i])
        else:
            return(data[i])

def part2(target):
    frontdata = data.copy()
    for a in data:
        backdata = frontdata.copy()
        for b in frontdata:
            if sum(backdata) != target:
                try:
                    backdata.remove(backdata[(len(backdata) - 1)])
                except:
                    break
            else:
                return(min(backdata) + max(backdata))
        frontdata.remove(a)

target = part1()
print("Part One Answer:", target)
print("Part Two Answer:", part2(target))
