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
    for i in range(len(gamma)):
        if gamma[i] == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    return(int(gamma, 2) * int(epsilon, 2))

def part2():
    def getoxygen(input):
        for num in range(len(input[0])):
            collector = {0:0, 1:0}
            oxygen = []
            common = "0"
            for line in input:
                if line[num] == "1":
                    collector[1] += 1
                else:
                    collector[0] += 1
            if collector[1] >= collector[0]:
                common = "1"
            for line in input:
                if line[num] == common:
                    oxygen.append(line)
            input = oxygen
            if len(oxygen) == 1:
                break
        return(oxygen[0])

    def getscrubber(input):
        for num in range(len(input[0])):
            collector = {0:0, 1:0}
            scrubber = []
            uncommon = "1"
            for line in input:
                if line[num] == "1":
                    collector[1] += 1
                else:
                    collector[0] += 1
            if collector[0] <= collector[1]:
                uncommon = "0"
            for line in input:
                if line[num] == uncommon:
                    scrubber.append(line)
            input = scrubber
            if len(scrubber) == 1:
                break
        return(scrubber[0])
    result = int(getoxygen(input), 2) * int(getscrubber(input), 2)
    return(result)
        
print("Part One Answer:", part1())
print("Part Two Answer:", part2())