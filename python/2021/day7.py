with open("C:\Scripts\Python\Advent of Code\day7input.txt") as fin:
    input = [int(i) for i in fin.read().strip().split(",")]

def part1():
    fuellist = []
    for num in range(0, max(input)):
        fuel = 0
        for crab in input:
            fuel += max(crab - num, num - crab)
        fuellist.append(fuel)
    return(min(fuellist))

def part2():
    fuellist = []
    for num in range(0, max(input)):
        fuel = 0
        for crab in input:
            maxx = max(crab - num, num - crab)
            for i in range(0, (maxx + 1)):
                fuel += i
        fuellist.append(fuel)
    return(min(fuellist))

print("Part One Answer:", part1())
print("Part Two Answer:", part2())