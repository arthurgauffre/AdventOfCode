#!//bin/env python3

import itertools

def evaluate_left_to_right(numbers, operators):
    current = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            current += numbers[i + 1]
        elif operators[i] == '*':
            current *= numbers[i + 1]
        elif operators[i] == '||':
            current = int(str(current) + str(numbers[i + 1]))
    return current

def checkCalibration(calibration):
    target = calibration[0]
    numbers = calibration[1]

    operator_combinations = itertools.product(['+', '*', '||'], repeat=len(numbers) - 1)

    for operators in operator_combinations:
        if evaluate_left_to_right(numbers, operators) == target:
            return True
    return False

def totalCalibration():
    total = 0
    calibrations = []

    with open('input.txt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        parts = line.split(':')
        test_value = int(parts[0])
        numbers = list(map(int, parts[1].strip().split(' ')))
        calibrations.append((test_value, numbers))

    for calibration in calibrations:
        if checkCalibration(calibration):
            total += calibration[0]
    return total

if __name__ == '__main__':
    print(f'Total Calibration: {totalCalibration()}')

