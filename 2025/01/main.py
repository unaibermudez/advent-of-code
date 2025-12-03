import sys

def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def solve_part1(lines):
    position = 50
    count = 0
    for line in lines:
        if not line: continue
        direction = line[0]
        number = int(line[1:])
        
        if direction == 'L':
            position = (position - number) % 100
        elif direction == 'R':
            position = (position + number) % 100
            
        if position == 0:
            count += 1
    return count

def solve_part2(lines):
    position = 50
    count = 0
    for line in lines:
        if not line: continue
        direction = line[0]
        number = int(line[1:])
        
        if direction == 'L':
            linear_pos = position - number
        elif direction == 'R':
            linear_pos = position + number
            
        # Count crossings of the 0/99 boundary
        crossings = abs(linear_pos // 100)
        count += crossings
        
        position = linear_pos % 100
            
        if position == 0:
            count += 1
    return count

def main():
    file_path = 'sample.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
    lines = open_file(file_path)
    result = solve_part1(lines)
    print(f"Password part 1: {result}")
    result = solve_part2(lines)
    print(f"Password part 2: {result}") # not correct 
    

if __name__ == '__main__':
    main()