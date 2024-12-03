#!//bin/env python3

import sys
import re

def uncorruptedMul():
    total = 0
    uncorruptedMul = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        uncorruptedMul.append(re.findall(r"mul\(\d+,\d+\)", line))
    for line in uncorruptedMul:
        for mul in line:
            total += int(mul.split('(')[1].split(',')[0]) * int(mul.split(',')[1].split(')')[0])

    return total

def uncorruptedDoMul():
    do = True
    total = 0
    uncorruptedMul = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        uncorruptedMul.append(re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", line))
    for line in uncorruptedMul:
        for instruc in line:
            if instruc == "don't()":
                do = False
            elif instruc == "do()":
                do = True
            elif do:
                total += int(instruc.split('(')[1].split(',')[0]) * int(instruc.split(',')[1].split(')')[0])

    return total


if __name__ == '__main__':
    print(f'uncorruptedMul: {uncorruptedMul()}')
    print(f'uncorruptedDoMul: {uncorruptedDoMul()}')