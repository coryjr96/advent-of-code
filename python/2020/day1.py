with open("day1input.txt") as fin:
    input = [int(i) for i in fin.read().strip().split("\n")]

def part1():
    for number in range(0, len(input)):
        for add in range(0, len(input)):
            sum = input[number] + input[add]
            if sum == 2020:
                return(input[number] * input[add])

def part2():
    for one in range(0, len(input)):
        for two in range(0, len(input)):
            for three in range(0, len(input)):
                sum = input[one] + input[two] + input[three]
                if sum == 2020:
                    return(input[one] * input[two] * input[three])

print("Part One Answer:", part1())
print("Part Two Answer:", part2())