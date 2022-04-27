from collections import Counter

with open("C:\Scripts\Python\Advent of Code\day5input.txt") as fin:
    data = fin.read().splitlines()

def part1():
    points = []
    for line in data:
        firstpoint, secondpoint = line.split('->')
        x1, y1 = tuple(map(int, firstpoint.split(',')))
        x2, y2 = tuple(map(int, secondpoint.split(',')))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    points.append((x,y))
    
    return len([point for point in Counter(points).values() if point > 1])

def part2():
    points = []
    for line in data:
        firstpoint, secondpoint = line.split('->')
        x1, y1 = tuple(map(int, firstpoint.split(',')))
        x2, y2 = tuple(map(int, secondpoint.split(',')))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    points.append((x,y))
        else:
            xinc = 1 if x1 < x2 else -1
            yinc = 1 if y1 < y2 else -1
            y = y1
            for x in range(x1, x2+xinc, xinc):
                points.append((x,y))
                y += yinc

    return len([point for point in Counter(points).values() if point > 1])

print("Part 1 answer: ", part1())
print("Part 2 answer: ", part2())