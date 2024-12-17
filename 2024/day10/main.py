#!//bin/env python3

dictTrailheads = {}

def checkTrailHead(topoMap, xTrailHead, yTrailHead, x, y, nb):
    if x < 0 or y < 0 or x >= len(topoMap[0]) or y >= len(topoMap):
        return
    if topoMap[y][x] == 9:
        if dictTrailheads.get((xTrailHead, yTrailHead)) is None:
            dictTrailheads[xTrailHead, yTrailHead] = [[x, y]]
        elif [x, y] not in dictTrailheads[xTrailHead, yTrailHead]:
            dictTrailheads[xTrailHead, yTrailHead].append([x, y])
        return
    if x + 1 < len(topoMap[0]) and topoMap[y][x + 1] == nb + 1:
        checkTrailHead(topoMap, xTrailHead, yTrailHead, x + 1, y, nb + 1)
    if x - 1 >= 0 and topoMap[y][x - 1] == nb + 1:
        checkTrailHead(topoMap, xTrailHead, yTrailHead, x - 1, y, nb + 1)
    if y + 1 < len(topoMap) and topoMap[y + 1][x] == nb + 1:
        checkTrailHead(topoMap, xTrailHead, yTrailHead, x, y + 1, nb + 1)
    if y - 1 >= 0 and topoMap[y - 1][x] == nb + 1:
        checkTrailHead(topoMap, xTrailHead, yTrailHead, x, y - 1, nb + 1)
    return

def parseTrailHead(topoMap):
    for y in range(len(topoMap)):
        for x in range(len(topoMap[y])):
            if topoMap[y][x] == 0:
                checkTrailHead(topoMap, x, y, x, y, 0)
    return topoMap

def nbTrailHead():
    total = 0
    topoMap = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        list = []
        for i in range(len(line)):
            list.append(int(line[i]))
        topoMap.append(list)
    parseTrailHead(topoMap)
    print(dictTrailheads)
    for list in dictTrailheads.values():
        total += len(list)
    return total

if __name__ == "__main__":
    print('nbTrailHead:', nbTrailHead())