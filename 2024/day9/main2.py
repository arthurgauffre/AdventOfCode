#!//bin/env python3

def freeDiskSpace(diskMap):
    for i in range(len(diskMap)):
        if diskMap[i] == -1:
            for j in range(-1, -len(diskMap), -1):
                if diskMap[j] != -1:
                    diskMap[i] = diskMap[j]
                    diskMap[j] = -1
                    break
            i -= 1
    if diskMap[-1] != -1:
        for i in range(len(diskMap)):
            if diskMap[i] == -1:
                diskMap[i] = diskMap[-1]
                diskMap[-1] = -1
                break

def checkDisk(diskMap):
    print(diskMap)
    for i in range(len(diskMap) - 1):
        if diskMap[i] == -1 and diskMap[i + 1] != -1:
            return False
    return True

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