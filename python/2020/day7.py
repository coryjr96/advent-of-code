with open("day7input.txt") as fin:
    preinput = [i for i in fin.read().strip().replace(" bags", "").split("\n")]
    input = []
    for line in preinput:
        input.append(line.replace(" bag", "").split(" contain "))
    splitrow = []
    part2input = []
    for line in input:
        splitrow = [line[0], line[1].replace(".", "").split(", ")]
        part2input.append(splitrow)

def part1():
    bags = ["shiny gold"]
    newbags = []
    allbags = []
    while True:
        for line in input:
            for bag in bags:
                if bag in line[1]:
                    if line[0] not in allbags:
                        newbags.append(line[0])
                        allbags.append(line[0])
        if len(newbags) == 0:
            break
        bags = newbags.copy()
        newbags = []
    return(len(allbags))

def part2():
    bags = ["shiny gold"]
    newbags = []
    allbags = []
    while True:
        for line in part2input:
            for bag in bags:
                if bag == line[0]:
                    for b in range(len(line[1])):
                        if line[1][0] != "no other":
                            for i in range(int(line[1][b][0])):
                                allbags.append(line[1][b][2:])
                                newbags.append(line[1][b][2:])
        if len(newbags) == 0:
            break
        bags = newbags.copy()
        newbags = []
    return(len(allbags))
        
print("Part One Answer:", part1())
print("Part Two Answer:", part2())