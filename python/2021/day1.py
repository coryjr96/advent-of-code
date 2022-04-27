with open("day1input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n")]
    input = []
    for line in preinput:
        input.append(int(line))

def part1():
    increased = 0
    for item in range(1, len(input)):
        if input[item - 1] < input[item]:
            increased += 1
    return(increased)

def part2():
    increased = 0
    for item in range(2, len(input)):
        group1 = input[item - 2] + input[item - 1] + input[item]
        group2 = input[item - 3] + input[item - 2] + input[item - 1]
        if group1 > group2:
            increased += 1
    return(increased)

print("Part One Answer:", part1())
print("Part Two Answer:", part2())