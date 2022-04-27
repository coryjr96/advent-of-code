with open("day2input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n")]
    input = []
    for line in preinput:
        input.append(line.split(" "))

def part1():
    horizontal = 0
    depth = 0
    for line in input:
        if line[0] == "forward":
            horizontal += int(line[1])
        elif line[0] == "down":
            depth += int(line[1])
        else:
            depth -= int(line[1])
    return(depth * horizontal)

def part2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in input:
        if line[0] == "down":
            aim += int(line[1])
        elif line[0] == "up":
            aim -= int(line[1])
        else:
            horizontal += int(line[1])
            depth += aim * int(line[1])
    return(depth * horizontal)

print("Part One Answer:", part1())
print("Part Two Answer:", part2())
