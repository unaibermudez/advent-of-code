import sys

def open_file(file_path):
    with open(file_path) as f:
        content = f.read().replace('\n', '')
        pairs = [p for p in content.split(',') if p]
    return pairs

def solve_part1(pairs):
    solution = 0
    for pair in pairs:
        from_, to_ = pair.split('-')
        for num in range(int(from_), int(to_)+1):
            num_str = str(num)
            length = len(num_str)
            if length % 2 == 0:
                mid = length // 2
                first_half = num_str[:mid]
                second_half = num_str[mid:]
                if first_half == second_half:
                    solution += num
            
    return solution

def is_periodic(num):
    s = str(num)
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            if s[:i] * (n // i) == s:
                return True
    return False

def solve_part2(pairs):
    solution = 0
    for pair in pairs:
        from_, to_ = pair.split('-')
        for num in range(int(from_), int(to_) + 1):
            if is_periodic(num):
                solution += num
    return solution

def main():
    file_path = 'sample.txt'
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
    pairs = open_file(file_path)
    result = solve_part1(pairs)
    print(f"Solution part 1: {result}")
    result2 = solve_part2(pairs)
    print(f"Solution part 2: {result2}")

if __name__ == '__main__':
    main()