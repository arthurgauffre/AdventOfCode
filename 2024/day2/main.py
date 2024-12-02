#!//bin/env python3

import sys

def checkReport(report):
    increasing = True
    if len(report) < 2:
        return True
    if report[0] > report[1]:
        increasing = False
    for i in range(len(report) - 1):
        if report[i] == report[i + 1]:
            return False
        if increasing:
            if report[i + 1] - report[i] > 3 or report[i + 1] - report[i] < 0:
                return False
        else:
            if report[i] - report[i + 1] > 3 or report[i] - report[i + 1] < 0:
                return False
    return True

def nbReportSafe():
    nbReportSafe = 0
    report = []
    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        for i in range(len(line.split())):
            report.append(int(line.split()[i]))
        if checkReport(report):
            nbReportSafe += 1
        report.clear()

    return nbReportSafe

if __name__ == '__main__':
    print(f'nbReportSafe: {nbReportSafe()}')