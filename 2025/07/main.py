import sys

def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def solve_part1(lines):
    first_line_s_index = lines[0].index('S')
    lines[1] = lines[1][:first_line_s_index] + '|' + lines[1][first_line_s_index+1:]

    res=0
    for i in range(1, len(lines)-2):
        for j in range(len(lines[i])):
            if lines[i][j] == '|':
                if lines[i+1][j] == '^' and i < len(lines) -1:
                    index = j
                    lines[i+1] = lines[i+1][:index-1] + '|' + lines[i+1][index] + '|' + lines[i+1][index+2:]
                    res+=1
                else:
                    index = j
                    lines[i+1] = lines[i+1][:index] + '|' + lines[i+1][index+1:]        
    return res         

def main():
    file_path = 'sample.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
    lines = open_file(file_path)
    result = solve_part1(lines)
    print(f"Password part 1: {result}")

    

if __name__ == '__main__':
    main()