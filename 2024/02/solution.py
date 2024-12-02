file_path = 'input.txt'

### FILE OPENING ###
def open_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

### PART 1 ###

def is_increasing(list):
    return all(int(list[i]) <= int(list[i+1]) for i in range(len(list)-1))

def is_decreasing(list):
    return all(int(list[i]) >= int(list[i+1]) for i in range(len(list)-1))

def is_valid(list):
    for i in range(len(list)-1):
        if abs(int(list[i]) - int(list[i+1])) < 1 or abs(int(list[i]) - int(list[i+1])) > 3:
            return False
    return True

def part1(lines):
    safe_lines = 0
    for line in lines:
        line_numbers = line.strip().split()
        if ((is_increasing(line_numbers) or is_decreasing(line_numbers)) and is_valid(line_numbers)):
            safe_lines += 1
    print(f'solution part 1: {safe_lines}')

### PART 2 ###

def is_valid_part1(line_numbers):
    return (is_increasing(line_numbers) or is_decreasing(line_numbers)) and is_valid(line_numbers)

def recursive_validate(list):
    for i in range(len(list)):
        new_list = list[:i] + list[i+1:]
        if is_valid_part1(new_list):
            return True
    return False


def part2(lines):
    safe_lines = 0
    for line in lines:
        line_numbers = line.strip().split()
        if (is_valid_part1(line_numbers)):
            safe_lines += 1
        else:
            if recursive_validate(line_numbers):
                safe_lines += 1
    print(f'solution part 2: {safe_lines}')


### MAIN ###
def main():
    lines = open_file(file_path)
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()