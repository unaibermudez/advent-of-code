import re
file_path = 'input.txt'

### FILE OPENING ###
def open_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

### PART 1 ###
def part1(lines):
    total = 0
    for line in lines:
        result = re.findall(r'mul\(\d+,\d+\)', line)
        for res in result:
            numbers = re.findall(r'\d+', res)
            total += int(numbers[0]) * int(numbers[1])

    print(f'solution part 1: {total}')

### PART 2 ###
def part2(lines):
    total = 0
    activated = True
    check_pattern = r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)"
    
    for line in lines:
        results = re.findall(check_pattern, line)
        for func in results:
            if func == "do()":
                activated = True
            elif func == "don't()":
                activated = False
            else:
                if activated:
                    numbers = re.findall(r'\d+', func)
                    total += int(numbers[0]) * int(numbers[1])

    print(f'solution part 2: {total}')

### MAIN ###
def main():
    lines = open_file(file_path)
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()