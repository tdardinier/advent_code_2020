l = [int(x) for x in open("input.txt", "r").readlines()]
print([x * y for x in l for y in l if x + y == 2020][0])
print([x * y * z for x in l for y in l for z in l if x + y + z == 2020][0])
