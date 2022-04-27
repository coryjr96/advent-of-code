with open("day12input.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]

def part1():
    northpercent = [0.75, 1.75, 2.75, 3.75, -0.25, -1.25, -2.25, -3.25]
    southpercent = [0.25, 1.25, 2.25, 3.25, -0.75, -1.75, -2.75, -3.75]
    westpercent = [0.5, -0.5, 1.5, -1.5, 2.5, -2.5, 3.5, -3.5]
    degrees = 0
    y = 0
    x = 0
    for line in range(len(data)):
        operator = data[line][0]
        value = int(data[line][1:])
        if operator == "E":
            x += value
        elif operator == "N":
            y += value
        elif operator == "W":
            x -= value
        elif operator == "S":
            y -= value
        elif operator == "L":
            degrees -= value
        elif operator == "R":
            degrees += value
        elif operator == "F":
            percentage = degrees / 360
            if degrees % 360 == 0:
                x += value
            elif percentage in westpercent:
                x -= value
            elif percentage in southpercent:
                y -= value
            elif percentage in northpercent:
                y += value
    return(abs(x) + abs(y))

print("Part One Answer:", part1())