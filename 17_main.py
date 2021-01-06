cube = [[[[x == "#" for x in line[:-1]] for line in open("input.txt", "r").readlines()]]]

def is_valid(cube, ww, xx, yy, zz):
    if zz >= 0 and zz < len(cube):
        if yy >= 0 and yy < len(cube[zz]):
            if xx >= 0 and xx < len(cube[zz][yy]):
                if ww >= 0 and ww < len(cube[zz][yy][xx]):
                    return True
    return False

def get_neighbours(cube, w, x, y, z):
    l = []
    for xx in range(x - 1, x + 2):
        for yy in range(y - 1, y + 2):
            for zz in range(z - 1, z + 2):
                for ww in range(w - 1, w + 2):
                    if xx != x or yy != y or zz != z or ww != w:
                        if is_valid(cube, ww, xx, yy, zz):
                            l.append((ww, xx, yy, zz))
    return l

def iterate(cube):
    ncube = []
    for z in range(-1, len(cube) + 1):
        zz = []
        for y in range(-1, len(cube[0]) + 1):
            yy = []
            for x in range(-1, len(cube[0][0]) + 1):
                xx = []
                for w in range(-1, len(cube[0][0][0]) + 1):
                    ww = False
                    if is_valid(cube, w, x, y, z) and cube[z][y][x][w]:
                        if 2 <= len([(www, xxx, yyy, zzz) for (www, xxx, yyy, zzz) in get_neighbours(cube, w, x, y, z) if cube[zzz][yyy][xxx][www]]) <= 3:
                            ww = True
                    else:
                        if len([(www, xxx, yyy, zzz) for (www, xxx, yyy, zzz) in get_neighbours(cube, w, x, y, z) if cube[zzz][yyy][xxx][www]]) == 3:
                            ww = True
                    xx.append(ww)
                yy.append(xx)
            zz.append(yy)
        ncube.append(zz)
    return ncube

for _ in range(6):
    cube = iterate(cube)
print(sum([sum([sum([sum(x) for x in y]) for y in z]) for z in cube]))
