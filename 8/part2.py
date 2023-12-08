import math
from itertools import cycle
def p2(f):
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    ans = []

    for curr in maps:
        if not curr.endswith("A"):
            continue
        visited = set()
        for count, (idx, d) in enumerate(cycle(enumerate(path)), start=1):
            prev, curr = curr, maps[curr][d == "R"]
            visited.add((curr, idx))
            if prev.endswith("Z") and (curr, idx) in visited:
                ans.append(count - 1)
                break

    return math.lcm(*ans)

print(p2(open("8/input.txt")))