with open("day112input.txt") as fin:
    data = [i for i in fin.read().strip().split("\n")]


def getacross(x, y):
    pass
def getupdown(x, y):
    pass
def getdiag(x, y):
    adjacents = ["", "", "", ""]
    for i in range(8):
        adjacents[0] += data[x + i][y + i] #going down right
        adjacents[1] += data[x + i][y - i] #going down left
        adjacents[2] += data[x - i][y + i] #going up right
        adjacents[3] += data[x - i][y - i] #going up left




print(diagonal)