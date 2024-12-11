#!//bin/env python3

dictAntinodes = {}

dictAntinodes = {}

def addAntinode(lines, x, y, total):
    antenna = lines[y][x]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == antenna:
                vector = [j - x, i - y]
                new_x, new_y = j + vector[0], i + vector[1]
                if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[i]):
                    if lines[new_y][new_x] == '.' or lines[new_y][new_x] == '#':
                        oldAntenna = dictAntinodes.get((new_x, new_y))
                        
                        if oldAntenna is None:
                            dictAntinodes[new_x, new_y] = [antenna]
                            lines[new_y][new_x] = '#'
                            total += 1
                        elif antenna not in oldAntenna:
                            oldAntenna.append(antenna)
                            dictAntinodes[new_x, new_y] = oldAntenna
                            lines[new_y][new_x] = '#'
                            total += 1
    return lines, total


def parseInput(lines, total):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != '.' and lines[y][x] != '#':
                lines, total = addAntinode(lines, x, y, total)
    return lines, total

def countAntinodes():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    for y in range(len(lines)):
        lines[y] = list(lines[y])
    lines, total = parseInput(lines, total)
    return total

if __name__ == "__main__":
    print('countAntinodes:', countAntinodes())