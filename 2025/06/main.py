import sys

def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def solve_part1(lines):
    result = 0
    operations = lines[-1].split()
    print(f"Operations: {operations}")
    lines = lines[:-1]
    for i in range(len(lines)):
        lines[i] = lines[i].split()
    print(f"Lines: {lines}")
    
    for i in range(len(lines[0])):
        if operations[i] == '+':
            line_result = 0
        else:
            line_result = 1
        for j in range(len(lines)):
            if operations[i] == '+':
                line_result += int(lines[j][i])
            else:
                line_result *= int(lines[j][i])

        result += line_result
    
    
    return result
    


def main():
    file_path = 'sample.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
    lines = open_file(file_path)
    result = solve_part1(lines)
    print(f"Password part 1: {result}")

    

if __name__ == '__main__':
    main()