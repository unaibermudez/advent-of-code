file_path= "8/input.txt"

with open(file_path, 'r') as file:
    lines = file.read().splitlines()

    instructions = list(lines[0])

    map= {}
    for i in range(2, len(lines)):
        node = lines[i].split('=')[0].replace(" ", "")
        direction_left = lines[i].split('=')[1].split('(')[1].split(',')[0].replace(" ", "")
        directions_right = lines[i].split('=')[1].split('(')[1].split(',')[1].split(')')[0].replace(" ", "")
        #add to map key = node, value = (direction_left, directions_right)
        map[node] = (direction_left, directions_right)
    
    #find in map the value 'AAA'
    actual = map['AAA']
    steps = 0
    found= False
    while not found:
        for instruction in instructions:
            if instruction == 'L':
                if  actual[0] == 'ZZZ':
                    steps += 1
                    found = True
                    break
                actual = map[actual[0]]
                steps += 1
            elif instruction == 'R':
                if  actual[1] == 'ZZZ':
                    steps += 1
                    found = True
                    break
                actual = map[actual[1]]
                steps += 1

    print(steps)
    print(found)


           
