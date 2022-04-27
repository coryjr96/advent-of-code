with open("day4input.txt") as fin:
    input = [i for i in fin.read().strip().split("\n\n")]
    frmtpassports = []
    for i in input:
        frmtpassports.append(i.replace("\n", " ").split(" "))

def part1():
    reqfields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passports = input.copy()
    for field in reqfields:
        scrub = []
        for i in passports:
            if field in i:
                scrub.append(i)
        passports = scrub
    return(passports)
            
def part2(passports):
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    hcl = ["a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    frmtpassports = []
    for i in passports:
        frmtpassports.append(i.replace("\n", " ").split(" "))
    finalpassports = frmtpassports.copy()
    for p in frmtpassports:
        remove = False
        for f in p:
            field = f.split(":")
            if field[0] == "byr":
                if int(field[1]) < 1920 or int(field[1]) > 2002:
                    finalpassports.remove(p)
                    break
            if field[0] == "iyr":
                if int(field[1]) < 2010 or int(field[1]) > 2020:
                    finalpassports.remove(p)
                    break
            if field[0] == "eyr":
                if int(field[1]) < 2020 or int(field[1]) > 2030:
                    finalpassports.remove(p)
                    break
            if field[0] == "hgt":
                if field[1][-2:] != "in" and field[1][-2:] != "cm":
                    finalpassports.remove(p)
                    break
                if field[1][-2:] == "in":
                    if int(field[1][:-2]) < 59 or int(field[1][:-2]) > 76:
                        finalpassports.remove(p)
                        break
                if field[1][-2:] == "cm":
                    if int(field[1][:-2]) < 150 or int(field[1][:-2]) > 193:
                        finalpassports.remove(p)
                        break
            if field[0] == "hcl":
                if len(field[1]) != 7:
                    finalpassports.remove(p)
                    break
                if field[1][0] != "#":
                    finalpassports.remove(p)
                    break
                for c in range(1, 6):
                    if field[1][c] not in hcl:
                        remove = True
                if remove != False:
                    finalpassports.remove(p)
                    break
            if field[0] == "ecl":
                if field[1] not in ecl:
                    finalpassports.remove(p)
                    break
            if field[0] == "pid":
                if len(field[1]) != 9:
                    finalpassports.remove(p)
                    break
    return(len(finalpassports))

    

passports = part1()
print("Part One Answer:", len(passports))
print("Part Two Answer:", part2(passports))