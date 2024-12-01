file_path= "6/input.txt"

with open(file_path, 'r') as f:
    lines = f.read().splitlines()
    #take the numbers from the first line
    times = [int(x) for x in lines[0].split(':')[1].split()]
    distance = [int(x) for x in lines[1].split(':')[1].split()]
    total = 1
    for i in range(len(times)):
        total_ways = 0
        for time_pressed in range(0, times[i]+1):
            distance_traveled = (times[i]-time_pressed) * time_pressed
            if distance_traveled > distance[i]:
                total_ways += 1
        
        total *=total_ways
    
    print(total)
        