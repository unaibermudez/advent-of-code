# https://www.reddit.com/r/adventofcode/comments/1pclp87/2025_day_01_both_partsgo_and_python_i_learned/
with open('./input.txt', 'r') as inputfile:
    rotations = [i.strip() for i in inputfile.readlines()]

state = 50   # the dial starts at 50 by default
counter = 0

def dial(state, direction, distance):
    x = 0
    clicks = 0
    if direction == 'L':
        y = state - distance
        clicks = ((state-1) // 100) - ((y-1) // 100)
        x = y % 100
    if direction == 'R':
        y = state + distance
        clicks = (y // 100) - (state // 100)
        x = y % 100
    return x, clicks

for move in rotations:
    direction = move[0]
    distance = int(move[1:])
    point, clicks = dial(state, direction, distance)
    counter += clicks
    state = point

print(counter)