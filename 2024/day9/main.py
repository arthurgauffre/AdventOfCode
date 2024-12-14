#!//bin/env python3

def nbFreeDiskSpace(diskMap, i):
    space = 0
    while i < len(diskMap) and diskMap[i] == -1:
        space += 1
        i += 1
    return space

def sizeFile(diskMap, i, id):
    space = 0
    while i > -len(diskMap) and diskMap[i] == id:
        i -= 1
        space += 1
    return space

def freeDiskSpace(diskMap):
    nbSpace = 0
    fileSpace = 0
    i = -1
    while i >-len(diskMap):
        if diskMap[i] != -1:
            fileSpace = sizeFile(diskMap, i, diskMap[i])
            for j in range(len(diskMap) + i):
                if diskMap[j] == -1:
                    nbSpace = nbFreeDiskSpace(diskMap, j)
                    if nbSpace >= fileSpace:
                        for k in range(fileSpace):
                            diskMap[j + k] = diskMap[i - k]
                        for k in range(fileSpace):
                            diskMap[i - k] = -1
            i -= fileSpace
        else:
            i -= 1

def parseDiskMap(line):
    diskMap = []
    id = 0
    for i in range(len(line)):
        if i % 2 == 0:
            for j in range(int(line[i])):
                diskMap.append(id)
            id += 1
        else:
            for j in range(int(line[i])):
                diskMap.append(-1)
    return diskMap

def fileSysCheckSum():
    total = 0
    diskMap = []
    with open('input.txt') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    diskMap = parseDiskMap(lines[0])
    freeDiskSpace(diskMap)
    for i in range(len(diskMap)):
        if diskMap[i] != -1:
            total += i * diskMap[i]
    return total

if __name__ == "__main__":
    print('fileSysCheckSum:', fileSysCheckSum())