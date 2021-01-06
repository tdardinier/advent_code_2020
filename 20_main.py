tiles = []
current_tile = [None, []]
for line in open("input.txt", "r").readlines():
    if line == "\n":
        tiles.append(current_tile)
        current_tile = [None, []]
    elif line[:4] == "Tile":
        current_tile[0] = line[5:-2]
    else:
        current_tile[1].append([x == "#" for x in line[:-1]])

n = len(tiles[0][1])
import math
m = int(math.sqrt(len(tiles)))

def rotateOnce(tile):
    return [[tile[y][-(x+1)] for y in range(len(tile))] for x in range(len(tile))]

def flip1(tile):
    return [[tile[x][-(y+1)] for y in range(len(tile))] for x in range(len(tile))]

def flip2(tile):
    return [[tile[-(x+1)][y] for y in range(len(tile))] for x in range(len(tile))]

def possibleTiles(tile):
    l = []
    for _ in range(2):
        for i in range(4):
            l.append(tile)
            tile = rotateOnce(tile)
        tile = flip1(tile)
    return l

def matchesTopBot(ttop, tbot):
    return ttop[n - 1] == tbot[0]

def matchesLeftRight(tleft, tright):
    return [r[n - 1] for r in tleft] == [r[0] for r in tright]

ntiles = []
for tile in tiles:
    for t in possibleTiles(tile[1]):
        ntiles.append((tile[0], t))

possibleTop = [set() for _ in range(len(ntiles))]
possibleBot = [set() for _ in range(len(ntiles))]
possibleLeft = [set() for _ in range(len(ntiles))]
possibleRight = [set() for _ in range(len(ntiles))]

for i in range(len(ntiles)):
    for j in range(len(ntiles)):
        if ntiles[i][0] != ntiles[j][0]:
            ti = ntiles[i][1]
            tj = ntiles[j][1]
            if matchesTopBot(ti, tj):
                possibleBot[i].add(j)
            if matchesTopBot(tj, ti):
                possibleTop[i].add(j)
            if matchesLeftRight(ti, tj):
                possibleRight[i].add(j)
            if matchesLeftRight(tj, ti):
                possibleLeft[i].add(j)

def getIDs(square):
    s = set()
    for row in square:
        for i in row:
            if i is not None:
                s.add(ntiles[i][0])
    return s

def possibleCandidates(square, i, j):
    s = getIDs(square)
    p = [x for x in range(len(ntiles)) if x not in square]
    if j - 1 >= 0:
        p = [x for x in p if x in possibleBot[square[i][j-1]]]
    if i - 1 >= 0:
        p = [x for x in p if x in possibleRight[square[i-1][j]]]
    return p

def nextIndices(i, j):
    if i + 1 < m:
        return (i + 1, j)
    else:
        return (0, j + 1)

def printTile(tile):
    for row in tile:
        s = ""
        for b in row:
            if b:
                s += "#"
            else:
                s += "."
        print(s)

def combine(t1, t2):
    return [t1[i] + t2[i] for i in range(len(t1))]

def removeBorders(t):
    return [r[1:-1] for r in t[1:-1]]

# s = [[14, 6, 64], [62, 30, 47], [54, 38, 20]]

seaMonster = []
seaMonster.append([x == "#" for x in "                  # "])
seaMonster.append([x == "#" for x in "#    ##    ##    ###"])
seaMonster.append([x == "#" for x in " #  #  #  #  #  #   "])

# i + 3 < len(...)
# j + 20 < len(...)
def seaMonsterAt(tile, i, j):
    b = True
    for ii in range(3):
        for jj in range(20):
            if seaMonster[ii][jj]:
                b = b and tile[i+ii][j+jj]
    return b

def seaMonsterInTile(tile):
    b = False
    for i in range(len(tile) - 3):
        for j in range(len(tile) - 20):
            b = b or seaMonsterAt(tile, i, j)
            if seaMonsterAt(tile, i, j):
                print("Found!", i, j)

    return b

def findMonsterRotate(s):
    tile = []
    for r in s:
        t = removeBorders(ntiles[r[0]][1])
        for tt in r[1:]:
            t = combine(t, removeBorders(ntiles[tt][1]))
        tile += t
    for p in possibleTiles(tile):
        if seaMonsterInTile(p):
            return p

# Line by line
def solve(square, i, j):
    print("solve", i, j)
    if i >= m or j >= m:
        print("Solution", findMonsterRotate(square))
        return (True, square)
    else:
        p = possibleCandidates(square, i, j)
        if len(p) == 0:
            return (False, None)
        else:
            (ii, jj) = nextIndices(i, j)
            for c in p:
                square[i][j] = c
                (b, s) = solve(square, ii, jj)
                if b:
                    return (b, s)
    return (False, None)


square = [[None for _ in range(m)] for _ in range(m)]
(b, s) = solve(square, 0, 0)

# Transposition
s = [[s[x][y] for x in range(len(s))] for y in range(len(s))]

corners = [s[0][0], s[0][-1], s[-1][0], s[-1][-1]]
ids = [int(ntiles[c][0]) for c in corners]
p = 1
for i in ids:
    p *= i
print(p)

tile = findMonsterRotate(s)

for i in range(len(tile) - 3):
    for j in range(len(tile) - 20):
        if seaMonsterAt(tile, i, j):
            for ii in range(3):
                for jj in range(20):
                    if seaMonster[ii][jj]:
                        tile[i+ii][j+jj] = False

c = 0
for r in tile:
    for rr in r:
        c += rr
print(c)
