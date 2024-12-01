file_path= "6/input.txt"

with open(file_path, 'r') as f:
    lines = f.read().splitlines()
    #take the numbers from the first line
    times = [int(x) for x in lines[0].split(':')[1].split()]
    distance = [int(x) for x in lines[1].split(':')[1].split()]
    #convert the list of integers into a single integer
    times = [int(''.join(map(str, times)))][0]
    distance = [int(''.join(map(str, distance)))][0]
    total = 1
    total_ways = 0
    for time_pressed in range(0, times):
        distance_traveled = (times-time_pressed) * time_pressed
        if distance_traveled > distance:
            total_ways += 1
    
    total *=total_ways

    print(total)
