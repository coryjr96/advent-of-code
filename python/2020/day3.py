with open("day3input.txt") as fin:
    input = [i for i in fin.read().strip().split("\n")]

def part1():
    xmove = 0
    trees = 0
    for line in input:
        if line[xmove] == "#":
            trees += 1
        xmove += 3
        if xmove > 30:
            xmove -= 31
    return(trees)

def part2():
    trees = []
    def gettrees(xinc, yinc):
        xmove = 0
        tree = 0
        if yinc == 1:
            for line in input:
                if line[xmove] == "#":
                    tree += 1
                xmove += xinc
                if xmove > 30:
                    xmove -= 31
            trees.append(tree)
        elif yinc == 2:
            for line in input:
                if input.index(line) % 2 == 0:
                    if line[xmove] == "#":
                        tree += 1
                    xmove += xinc
                    if xmove > 30:
                        xmove -= 31
            trees.append(tree)
    gettrees(1, 1)
    gettrees(3, 1)
    gettrees(5, 1)
    gettrees(7, 1)
    gettrees(1, 2)
    return(trees[0] * trees[1] * trees[2] * trees[3] * (trees[4] - 1))

print("Part One Answer:", part1())
print("Part Two Answer:", part2())