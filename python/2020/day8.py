with open("day8input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n")]          
    data = []
    for line in preinput:
        data.append(line.split(" "))

def part1():
    accumulator = 0
    hitlines = []
    jump = 0
    while jump not in hitlines:
        if data[jump][0] == "acc":
            if data[jump][1][0] == "+":
                accumulator += int(data[jump][1][1:])
            else:
                accumulator -= int(data[jump][1][1:])
            hitlines.append(jump)
            jump += 1
        if data[jump][0] == "nop":
            hitlines.append(jump)
            jump += 1
        if data[jump][0] == "jmp":
            hitlines.append(jump)
            if data[jump][1][0] == "+":
                jump += int(data[jump][1][1:])
            else:
                jump -= int(data[jump][1][1:])
    return(accumulator)

def part2():
    for line in range(len(data)):
        originalline = data[line][0]
        if data[line][0] == "nop":
            data[line][0] = "jmp"
        elif data[line][0] == "jmp":
            data[line][0] = "nop"
        accumulator = 0
        hitlines = []
        jump = 0
        try:
            while jump not in hitlines:
                if data[jump][0] == "acc":
                    if data[jump][1][0] == "+":
                        accumulator += int(data[jump][1][1:])
                    else:
                        accumulator -= int(data[jump][1][1:])
                    hitlines.append(jump)
                    jump += 1
                if data[jump][0] == "nop":
                    hitlines.append(jump)
                    jump += 1
                if data[jump][0] == "jmp":
                    hitlines.append(jump)
                    if data[jump][1][0] == "+":
                        jump += int(data[jump][1][1:])
                    else:
                        jump -= int(data[jump][1][1:])
            data[line][0] = originalline
        except:
            return(accumulator)


print("Part One Answer:", part1())
print("Part Two Answer:", part2())
