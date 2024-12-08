#!//bin/env python3

import itertools

def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def checkCalibration(calibration):
    target = calibration[0]
    numbers = calibration[1]

    operator_combinations = itertools.product(['+', '*'], repeat=len(numbers) - 1)

    for operators in operator_combinations:
        if evaluate_left_to_right(numbers, operators) == target:
            return True
    return False

def totalCalibration():
    total = 0
    calibrations = []
    calibrationsTmp = []
    with open('input.txt') as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        calibrationsTmp.append(int(line.split(':')[0]))
        calibrationsTmp.append((line.split(':')[1].strip().split(' ')))
        for i in range(len(calibrationsTmp[1])):
            calibrationsTmp[1][i] = int(calibrationsTmp[1][i])
        calibrations.append(calibrationsTmp)
        calibrationsTmp = []
    for calibration in calibrations:
        if checkCalibration(calibration):
            total += calibration[0]
    return total




if __name__ == '__main__':
    print(f'totalCalibration: {totalCalibration()}')
