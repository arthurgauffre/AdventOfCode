#!//bin/env python3

import sys

def totalDistance():
    totalDistance = 0
    list1 = []
    list2 = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            totalDistance += list1[i] - list2[i]
        else:
            totalDistance += list2[i] - list1[i]
    return totalDistance

def similarityScore():
    score = 0
    nbPairs = 0
    list1 = []
    list2 = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    for n1 in list1:
        for n2 in list2:
            if n1 == n2:
                nbPairs += 1
        score += n1 * nbPairs
        nbPairs = 0
    return score

if __name__ == '__main__':
    print(f'totalDistance: {totalDistance()}')
    print(f'similarity score: {similarityScore()}')