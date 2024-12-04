file_path = 'input.txt'

### FILE OPENING ###
def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

### PART 1 ###
def count_word(grid, word):
    n, m = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Horizontal (both directions)
    for row in grid:
        line = "".join(row)
        count += line.count(word)
        count += line[::-1].count(word)

    # Vertical (both directions)
    for col in range(m):
        line = "".join(grid[row][col] for row in range(n))
        count += line.count(word)
        count += line[::-1].count(word)

    # Diagonal (both directions)
    # Top-left to bottom-right and bottom-left to top-right
    for d in range(-n + 1, m):  # Range to cover all diagonals
        line1 = "".join(grid[i][i - d] for i in range(max(0, d), min(n, m + d)))
        line2 = "".join(grid[i][n - 1 - i + d] for i in range(max(0, d), min(n, m + d)))
        count += line1.count(word)
        count += line1[::-1].count(word)
        count += line2.count(word)
        count += line2[::-1].count(word)

    return count

def part1(lines):
    # Convert the input into a grid of characters
    grid = [list(line) for line in lines]
    word = "XMAS"
    result = count_word(grid, word)
    print(f"Occurrences of '{word}': {result}")

### PART 2 ###
def find_xmas_pattern(grid,line, col):
    try:
        top_left = grid[line-1][col-1]
        top_right = grid[line-1][col+1]
        bottom_left = grid[line+1][col-1]
        bottom_right = grid[line+1][col+1]
        if ((top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")) and ((top_right == "M" and bottom_left == "S")or (top_right == "S" and bottom_left == "M")):
            return True
        else:
            return False
    except IndexError:
        return False


def count_xmas_patterns(grid):
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "A":
                if(find_xmas_pattern(grid, i, j)):
                    count += 1
    return count


def part2(lines):
    # Convert the input into a grid of characters
    grid = [list(line) for line in lines]
    result = count_xmas_patterns(grid)
    print(f"Number of 'X-MAS' patterns: {result}")


### MAIN ###
def main():
    lines = open_file(file_path)
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()
