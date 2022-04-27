with open("C:\Scripts\Python\Advent of Code\day8input.txt") as fin:
    input = [i for i in fin.read().strip().split("\n")] 

def part1():
    dict = {1:0, 4:0, 7:0, 8:0}
    outputvals = [i.split("|")[1].strip().split(" ") for i in input]
    for output in outputvals:
        for signal in output:
            if len(signal) == 7:
                dict[8] += 1
            elif len(signal) == 4:
                dict[4] += 1
            elif len(signal) == 3:
                dict[7] += 1
            elif len(signal) == 2:
                dict[1] += 1
    return(sum(dict.values()))

def part2():
    inputvals = [i.split("|")[0].strip().split(" ") for i in input]
    outputvals = [i.split("|")[1].strip().split(" ") for i in input]
    totalsum = 0
    for i in range(len(input)):
        dict = {}
        for signal in inputvals[i]:
            if len(signal) == 7:
                dict[8] = signal
            elif len(signal) == 4:
                dict[4] = signal
            elif len(signal) == 3:
                dict[7] = signal
            elif len(signal) == 2:
                dict[1] = signal
        for signal in inputvals[i]:
            if len(signal) == 6:
                if set(dict[4]).issubset(set(signal)):
                    dict[9] = signal
                if set(dict[1]).issubset(set(signal)):
                    dict[0] = signal
                else:
                    dict[6] = signal
        for signal in inputvals[i]:
            if len(signal) == 5:
                if set(signal).issubset(set(dict[6])):
                    dict[5] = signal
                elif set(dict[1]).issubset(set(signal)):
                    dict[3] = signal
                else:
                    dict[2] = signal
        number = []
        for signal in outputvals[i]:
            for key, value in dict.items():
                if set(signal) == set(value):
                    number.append(str(key))
        number = int(''.join(number))
        totalsum += number
    
    return(totalsum)
    
print("Part One Answer:", part1())
print("Part Two Answer:", part2())
