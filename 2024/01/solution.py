file_path = 'input.txt'

def open_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
    return lines

def part1(lines):
    left = []
    right = []
    for line in lines:
        line = line.strip().split()
        left.append(line[0])
        right.append(line[-1])

    left.sort()
    right.sort()
    diff = 0
    for i in range(len(left)):
        diff += abs(int(left[i]) - int(right[i]))

    print(f'solution part 1: {diff}')

def part2(lines):
    left = []
    right = []
    for line in lines:
        line = line.strip().split()
        left.append(line[0])
        right.append(line[-1])

    similarity_score = 0
    for number in left:
        count = right.count(number)
        similarity_score += count*int(number)

    print(f'solution part 2: {similarity_score}')


def main():
    lines = open_file(file_path)
    part1(lines)
    part2(lines)

if __name__ == '__main__':
    main()