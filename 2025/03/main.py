import sys

def open_file(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def solve_part1(lines):
    volt_sum = 0
    for line in lines:
        max_volt = 0
        for i in range(len(line)):
            for j in range(i+1, len(line)):
                if i != j:
                    max_volt = max(max_volt, int(line[i] + line[j]))
        volt_sum += max_volt
    return volt_sum

def solve_part2(lines):
    volt_sum = 0
    for line in lines:        
        # This problem likely refers to finding the largest 12-digit number that can be formed
        # by selecting 12 digits from the input 'line' while maintaining their relative order.
        # This is a classic "find largest number by removing k digits" type problem.
        
        k = len(line) - 12  # Number of digits to remove
        
        stack = []
        for digit in line:
            while stack and k > 0 and stack[-1] < digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If still k > 0, remove from the end (for cases like "1111", k=2 -> "11")
        while k > 0:
            stack.pop()
            k -= 1            

        # The result should be exactly 12 digits long
        if len(stack) > 12:
            stack = stack[:12]

        largest_12_digit_num = int("".join(stack))
        volt_sum += largest_12_digit_num
    return volt_sum
    

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