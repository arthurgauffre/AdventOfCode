#!//bin/env python3

import re

def checkUpdate(pagesRules, update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            for rule in pagesRules:
                if rule[0] == update[j] and rule[1] == update[i]:
                    return False
    return True

def middlePageNumber():
    pagesRules = []
    updates = []
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r"\d+\|\d+", line):
            pagesRules.append([int(line.split('|')[0]), int(line.split('|')[1])])
        if re.search(r"\d+,", line):
            updates.append(list(map(int, line.split(','))))
    
    for update in updates:
        if checkUpdate(pagesRules, update):
            total += update[(len(update) - 1) // 2]
    return total

def sortUpdate(update, pagesRules):
    while not checkUpdate(pagesRules, update):
        for i in range(len(update)):
            for j in range(i+1, len(update)):
                for rule in pagesRules:
                    if rule[0] == update[j] and rule[1] == update[i]:
                        update[i], update[j] = update[j], update[i]
    return update

def middlePageNumber2():
    pagesRules = []
    updates = []
    total = 0
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        if re.search(r"\d+\|\d+", line):
            pagesRules.append([int(line.split('|')[0]), int(line.split('|')[1])])
        if re.search(r"\d+,", line):
            updates.append(list(map(int, line.split(','))))
    
    for update in updates:
        if not checkUpdate(pagesRules, update):
            update = sortUpdate(update, pagesRules)
            total += update[(len(update) - 1) // 2]
    return total


if __name__ == '__main__':
    print(f'middlePageNumber: {middlePageNumber()}')
    print(f'middlePageNumber2: {middlePageNumber2()}')