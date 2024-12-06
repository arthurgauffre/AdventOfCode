#!//bin/env python3

import re

def guardPattern(maps, guardPosistions, directions):
    directionsTmp = directions.copy()
    guardPosistionsTmp = guardPosistions.copy()
    nbWalked = 0
    while guardPosistionsTmp[0] >= 0 and guardPosistionsTmp[0] < len(maps[0]) and guardPosistionsTmp[1] >= 0 and guardPosistionsTmp[1] < len(maps):
        if nbWalked > len(maps) * len(maps[0]):
            return True
        if directionsTmp[0] == 1:
            if guardPosistionsTmp[0] + 1 < len(maps[0]) and maps[guardPosistionsTmp[1]][guardPosistionsTmp[0] + 1] == '#':
                directionsTmp = [0, 1]
            else:
                guardPosistionsTmp[0] += 1
        elif directionsTmp[0] == -1:
            if guardPosistionsTmp[0] - 1 >= 0 and maps[guardPosistionsTmp[1]][guardPosistionsTmp[0] - 1] == '#':
                directionsTmp = [0, -1]
            else:
                guardPosistionsTmp[0] -= 1
        elif directionsTmp[1] == 1:
            if guardPosistionsTmp[1] + 1 < len(maps) and maps[guardPosistionsTmp[1] + 1][guardPosistionsTmp[0]] == '#':
                directionsTmp = [-1, 0]
            else:
                guardPosistionsTmp[1] += 1
        elif directionsTmp[1] == -1:
            if guardPosistionsTmp[1] - 1 >= 0 and maps[guardPosistionsTmp[1] - 1][guardPosistionsTmp[0]] == '#':
                directionsTmp = [1, 0]
            else:
                guardPosistionsTmp[1] -= 1
        nbWalked += 1
    return False

def nbObstaclePossibility():
    total = 0
    directions = [0, 0]
    guardPosistions =  [0, 0]
    maps = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        maps.append(list(line.strip()))
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == '^':
                directions = [0, -1]
                guardPosistions = [x, y]
            if maps[y][x] == 'v':
                directions = [0, 1]
                guardPosistions = [x, y]
            if maps[y][x] == '>':
                directions = [1, 0]
                guardPosistions = [x, y]
            if maps[y][x] == '<':
                directions = [-1, 0]
                guardPosistions = [x, y]
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == '.':
                maps[y][x] = '#'
                if guardPattern(maps, guardPosistions, directions):
                    total += 1
                maps[y][x] = '.'
    return total




if __name__ == '__main__':
    print(f'nbObstaclePossibility: {nbObstaclePossibility()}')
