#!//bin/env python3

dictAntinodes = {}

def addAntinode(lines, x, y):
    antenna = lines[y][x]
    if dictAntinodes.get((x, y)) is None:
        dictAntinodes[x, y] = [antenna]
    else:
        dictAntinodes[x, y].append(antenna)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == antenna:
                vector = [j - x, i - y]
                if vector[0] == 0 and vector[1] == 0:
                    continue
                new_x, new_y = j + vector[0], i + vector[1]
                while 0 <= new_y < len(lines) and 0 <= new_x < len(lines[i]):
                        oldAntenna = dictAntinodes.get((new_x, new_y))
                        
                        if oldAntenna is None:
                            dictAntinodes[new_x, new_y] = [antenna]
                        elif antenna not in oldAntenna:
                            oldAntenna.append(antenna)
                            dictAntinodes[new_x, new_y] = oldAntenna
                        new_x += vector[0]
                        new_y += vector[1]
                new_x, new_y = j + vector[0], i + vector[1]
                while 0 <= new_y < len(lines) and 0 <= new_x < len(lines[i]):
                        oldAntenna = dictAntinodes.get((new_x, new_y))
                        
                        if oldAntenna is None:
                            dictAntinodes[new_x, new_y] = [antenna]
                        elif antenna not in oldAntenna:
                            oldAntenna.append(antenna)
                            dictAntinodes[new_x, new_y] = oldAntenna
                        new_x -= vector[0]
                        new_y -= vector[1]
    return lines


def parseInput(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != '.' and lines[y][x] != '#':
                lines = addAntinode(lines, x, y)
    return lines

def countAntinodes():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    for y in range(len(lines)):
        lines[y] = list(lines[y])
    lines = parseInput(lines)
    total = len(dictAntinodes)
    return total

if __name__ == "__main__":
    print('countAntinodes:', countAntinodes())