with open("day3input.txt") as fin:
    input = [i for i in fin.read().strip().split("\n")]

def part1():
    gamma = ""
    epsilon = ""
    collector = {0: 0, 1: 0}
    for i in range(len(input[0])):
        collector = {0: 0, 1: 0}
        for line in input:
            if line[i] == "0":
                collector[0] += 1
            else:
                collector[1] += 1
        if collector[0] < collector[1]:
            gamma += "1"
        else:
            gamma += "0"
    print(gamma)

part1()