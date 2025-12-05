def parse_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    ranges = []
    ids = []
    parsing_ranges = True

    for line in lines:
        if not line:
            parsing_ranges = False
            continue
        
        if parsing_ranges:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
        else:
            ids.append(int(line))
    return ranges, ids

def solve_part_1():
    ranges, ids = parse_input('input.txt')

    fresh_count = 0
    for ingredient_id in ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1
            print(f"Ingredient ID {ingredient_id} is fresh.")
        else:
            print(f"Ingredient ID {ingredient_id} is spoiled.")

    print(f"Total fresh ingredients: {fresh_count}")

def solve_part_2():
    ranges, _ = parse_input('input.txt')
    
    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    
    merged = []
    if not ranges:
        print("Total fresh ingredients (ranges union): 0")
        return

    current_start, current_end = ranges[0]
    
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        
        # Merge overlapping or adjacent intervals
        # e.g. [3, 5] and [6, 8] cover 3,4,5,6,7,8 which is [3, 8]
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    merged.append((current_start, current_end))
    
    total_count = sum(end - start + 1 for start, end in merged)
    print(f"Total fresh ingredients (ranges union): {total_count}")

if __name__ == "__main__":
    # solve_part_1()
    solve_part_2()
