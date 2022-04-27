with open("day6input.txt") as fin:
    preinput = [i for i in fin.read().strip().split("\n\n")]
    input = []
    for i in preinput:
        input.append(i.split("\n"))

def part1():
    sum = 0
    for group in input:
        answers = []
        for person in group:
            for letter in range(len(person)):
                if person[letter] not in answers:
                    answers.append(person[letter])
        sum += len(answers)
    return(sum)

def part2():
    sum = 0
    for group in input:
        answers = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
        for person in group:
            for letter in range(len(person)):
                answers[person[letter]] += 1
        for key in answers:
            if answers[key] == len(group):
                sum += 1
    return(sum)

print("Part One Answer:", part1())
print("Part Two Answer:", part2())