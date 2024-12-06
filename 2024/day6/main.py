#!//bin/env python3

import re

def guardPattern(maps, guardPosistions, directions):
    while guardPosistions[0] >= 0 and guardPosistions[0] < len(maps[0]) and guardPosistions[1] >= 0 and guardPosistions[1] < len(maps):
        maps[guardPosistions[1]][guardPosistions[0]] = 'X'
        if directions[0] == 1:
            if guardPosistions[0] + 1 < len(maps[0]) and maps[guardPosistions[1]][guardPosistions[0] + 1] == '#':
                directions = [0, 1]
            else:
                guardPosistions[0] += 1
        elif directions[0] == -1:
            if guardPosistions[0] - 1 >= 0 and maps[guardPosistions[1]][guardPosistions[0] - 1] == '#':
                directions = [0, -1]
            else:
                guardPosistions[0] -= 1
        elif directions[1] == 1:
            if guardPosistions[1] + 1 < len(maps) and maps[guardPosistions[1] + 1][guardPosistions[0]] == '#':
                directions = [-1, 0]
            else:
                guardPosistions[1] += 1
        elif directions[1] == -1:
            if guardPosistions[1] - 1 >= 0 and maps[guardPosistions[1] - 1][guardPosistions[0]] == '#':
                directions = [1, 0]
            else:
                guardPosistions[1] -= 1
    return maps

def nbDistinctPosition():
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
    maps = guardPattern(maps, guardPosistions, directions)
    for row in maps:
        for cell in row:
            if cell == 'X':
                total += 1
    return total




if __name__ == '__main__':
    print(f'nbDistinctPosition: {nbDistinctPosition()}')
