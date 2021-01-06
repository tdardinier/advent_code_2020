b = set()

for lline in open("input.txt", "r").readlines():
    line = lline[:-1]
    i = 0
    (x, y) = (0, 0)
    while i < len(line):
        if line[i] == "e":
            x += 2
            i -= 1
        elif line[i] == "w":
            x -= 2
            i -= 1
        elif line[i:i+2] == "se":
            x += 1
            y += 1
        elif line[i:i+2] == "sw":
            x -= 1
            y += 1
        elif line[i:i+2] == "nw":
            x -= 1
            y -= 1
        elif line[i:i+2] == "ne":
            x += 1
            y -= 1
        i += 2
    if (x, y) in b:
        print("Removing...")
        b.remove((x, y))
    else:
        b.add((x, y))

def find_bound(b):
    n = 0
    for (x, y) in b:
        n = max(n, abs(x))
        n = max(n, abs(y))
    return n + 1

n = find_bound(b)
bb = set()

for i in range(100):
    for x in range(-n, n+1):
        for y in range(-n, n+1):
            neighbours = set()
            neighbours.add((x + 1, y + 1))
            neighbours.add((x + 1, y - 1))
            neighbours.add((x - 1, y + 1))
            neighbours.add((x - 1, y - 1))
            neighbours.add((x - 2, y))
            neighbours.add((x + 2, y))
            neighbours = neighbours.intersection(b)
            if (x, y) in b:
                if not (len(neighbours) == 0 or len(neighbours) > 2):
                    bb.add((x, y))
            elif len(neighbours) == 2:
                bb.add((x, y))
    b = bb
    bb = set()
    n = find_bound(b)
    print(i + 1, len(b))
        
