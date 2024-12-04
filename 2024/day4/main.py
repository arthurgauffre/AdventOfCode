#!//bin/env python3

import sys
import re

def nbXMAX():
    total = 0
    diagonals = []
    verticals = []
    nbXMAX = []
    with open('input.txt') as f:
        lines = f.readlines()
    
    for line in lines:
        nbXMAX.append(re.findall(r"XMAS", line))
        nbXMAX.append(re.findall(r"SAMX", line))

    for index in range(len(lines)):
        for line in lines:
            if index < len(line):
                verticals.append(line[index])
        nbXMAX.append(re.findall(r"XMAS", ''.join(verticals)))
        nbXMAX.append(re.findall(r"SAMX", ''.join(verticals)))
        verticals = []


    for y in range(len(lines) - 1, -1, -1):
        x = 0
        while y < len(lines):
            diagonals.append(lines[y][x])
            x += 1
            y += 1
        nbXMAX.append(re.findall(r"XMAS", ''.join(diagonals)))
        nbXMAX.append(re.findall(r"SAMX", ''.join(diagonals)))
        diagonals = []
    
    for x in range(1, len(lines)):
        y = 0
        while x < len(lines):
            diagonals.append(lines[y][x])
            x += 1
            y += 1
        nbXMAX.append(re.findall(r"XMAS", ''.join(diagonals)))
        nbXMAX.append(re.findall(r"SAMX", ''.join(diagonals)))
        diagonals = []

    for y in range(len(lines)):
        x = 0
        while y >= 0:
            diagonals.append(lines[y][x])
            x += 1
            y -= 1
        nbXMAX.append(re.findall(r"XMAS", ''.join(diagonals)))
        nbXMAX.append(re.findall(r"SAMX", ''.join(diagonals)))
        diagonals = []

    for x in range(1, len(lines)):
        y = len(lines) - 1
        while x < len(lines):
            diagonals.append(lines[y][x])
            x += 1
            y -= 1
        nbXMAX.append(re.findall(r"XMAS", ''.join(diagonals)))
        nbXMAX.append(re.findall(r"SAMX", ''.join(diagonals)))
        diagonals = []

    for line in nbXMAX:
        total += len(line)

    return total

def nbXMAX2():
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if x + 2 < len(lines[y]) and y + 2 < len(lines):
                if (lines[y][x] == 'M' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x + 2] == 'S') or (lines[y][x] == 'S' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x + 2] == 'M'):
                    if (lines[y][x + 2] == 'M' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x] == 'S') or (lines[y][x + 2] == 'S' and lines[y + 1][x + 1] == 'A' and lines[y + 2][x] == 'M'):
                        total += 1
    return total


if __name__ == '__main__':
    print(f'nbXMAX: {nbXMAX()}')
    print(f'nbXMAX2: {nbXMAX2()}')