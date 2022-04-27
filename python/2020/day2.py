with open("day2input.txt") as fin:
    input = [i for i in fin.read().strip().split("\n")]
    req = []
    password = []
    for i in input:
        line = i.strip().split(":")
        req.append(line[0])
        password.append(line[1].strip())
    amount = []
    letter = []
    for i in req:
        line = i.split(" ")
        amount.append(line[0])
        letter.append(line[1])
    min = []
    max  = []
    for i in amount:
        line = i.split("-")
        min.append(line[0])
        max.append(line[1])

def part1():
    count = 0
    for pwd in range(len(letter)):
        if password[pwd].count(letter[pwd]) >= int(min[pwd]) and password[pwd].count(letter[pwd]) <= int(max[pwd]):
            count += 1
        else:
            pass
    return(count)

def part2():
    count = 0
    for pwd in range(len(letter)):
        if password[pwd][int(min[pwd]) - 1] == letter[pwd] and password[pwd][int(max[pwd]) - 1] != letter[pwd]:
            count += 1
        elif password[pwd][int(min[pwd]) - 1] != letter[pwd] and password[pwd][int(max[pwd]) - 1] == letter[pwd]:
            count += 1
        else:
            pass
    return(count)

print("Part One Answer:", part1())
print("Part Two Answer:", part2())