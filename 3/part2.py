"""
--- Part Two ---
no funciona bien

"""

import re

file_path = "3/input.txt"

# Define a function to check if a position is valid (inside the grid)
def is_valid_position(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

# Define a function to check if a character is a symbol
def is_symbol(char):
    return not char.isalnum() and char != '.'

# Define the directions to check around a number (the 4 positions around it)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

with open(file_path, 'r') as file:
    lines = [list(line.rstrip()) for line in file.readlines()]
    total_sum = 0
    total_gear_ratio = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                numbers = []
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    number = ''
                    while is_valid_position(x, y, len(lines), len(lines[i])) and lines[x][y].isdigit():
                        number += lines[x][y]
                        x, y = x + dx, y + dy
                    if number:
                        numbers.append(int(number))
                if len(numbers) == 2:
                    total_gear_ratio += numbers[0] * numbers[1]
        for match in re.finditer(r'\d+', ''.join(lines[i])):
            number = int(match.group())
            number_start_position = match.start()
            number_end_position = match.end()
            valid_number = False
            for dx, dy in directions:
                for pos in range(number_start_position, number_end_position):
                    if is_valid_position(i + dx, pos + dy, len(lines), len(lines[i])) and is_symbol(lines[i + dx][pos + dy]):
                        valid_number = True
                        break
                if valid_number:
                    break
            if valid_number:
                total_sum += number
    print(total_sum)
    print(total_gear_ratio)