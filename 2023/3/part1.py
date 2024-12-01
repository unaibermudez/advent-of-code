import re
file_path = "3/input.txt"

# Define a function to check if a position is valid (inside the grid)
def is_valid_position(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

# Define a function to check if a character is a symbol
def is_symbol(char):
    return not char.isalnum() and char != '.'

# Define the directions to check around a number (the 8 positions around it)
directions = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0]

with open(file_path, 'r') as file:
    lines = [list(line.rstrip()) for line in file.readlines()]
    total_sum = 0
    for i in range(len(lines)):
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