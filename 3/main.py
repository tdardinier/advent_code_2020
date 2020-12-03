M = [[x == "#" for x in l[:-1]] for l in open("input.txt", "r").readlines()]

(slopes, m) = ([(1, 1), (5, 1), (7, 1), (1, 2), (3, 1)], 1)

for (sx, sy) in slopes:
    (x, y, c) = (0, 0, 0)
    while y < len(M):
        (c, x, y) = (c + M[y][x % len(M[0])], x + sx, y + sy)
    m *= c

print(c, m)
