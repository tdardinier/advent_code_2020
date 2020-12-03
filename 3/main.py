M = [[x == "#" for x in l[:-1]] for l in open("input.txt", "r").readlines()]

(slopes, m) = ([(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)], 1)

for (i, (sx, sy)) in enumerate(slopes):
    (x, y, c) = (0, 0, 0)
    while y < len(M):
        (c, x, y) = (c + M[y][x % len(M[0])], x + sx, y + sy)
    if i == 0: print(c)
    m *= c

print(m)
