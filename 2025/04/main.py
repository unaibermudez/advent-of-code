import sys

def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def solve_part1(lines):
    can_be_accessed = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            n_adjacents = 0
            if lines[i][j] == '@':
                if i > 0 and lines[i-1][j] == '@':
                    n_adjacents += 1
                if i < len(lines) - 1 and lines[i+1][j] == '@':
                    n_adjacents += 1
                if j > 0 and lines[i][j-1] == '@':
                    n_adjacents += 1
                if j < len(lines[i]) - 1 and lines[i][j+1] == '@':
                    n_adjacents += 1
                if i > 0 and j > 0 and lines[i-1][j-1] == '@':
                    n_adjacents += 1
                if i > 0 and j < len(lines[i]) - 1 and lines[i-1][j+1] == '@':
                    n_adjacents += 1
                if i < len(lines) - 1 and j > 0 and lines[i+1][j-1] == '@':
                    n_adjacents += 1
                if i < len(lines) - 1 and j < len(lines[i]) - 1 and lines[i+1][j+1] == '@':
                    n_adjacents += 1
                if n_adjacents < 4:
                    can_be_accessed += 1

    return can_be_accessed

def part1_replacement(lines):
    new_lines = [list(row) for row in lines]
    to_replace = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            n_adjacents = 0
            if lines[i][j] == '@':
                # Check all 8 neighbors
                for r_offset in [-1, 0, 1]:
                    for c_offset in [-1, 0, 1]:
                        if r_offset == 0 and c_offset == 0:
                            continue # Skip the cell itself
                        
                        ni, nj = i + r_offset, j + c_offset
                        
                        if 0 <= ni < len(lines) and 0 <= nj < len(lines[ni]) and lines[ni][nj] == '@':
                            n_adjacents += 1
                
                if n_adjacents < 4:
                    to_replace.append((i, j))
    
    for r, c in to_replace:
        new_lines[r][c] = 'X'

    return ["".join(row) for row in new_lines]


def solve_part2(lines):
    result = 0
    can_be_accessed = solve_part1(lines)
    while can_be_accessed > 0:
        result += can_be_accessed
        lines = part1_replacement(lines)
        can_be_accessed = solve_part1(lines)
    return result
    

def main():
    file_path = 'sample.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
    lines = open_file(file_path)
    result = solve_part1(lines)
    print(f"Result part 1: {result}")
    result = solve_part2(lines)
    print(f"Password part 2: {result}") 
    

if __name__ == '__main__':
    main()