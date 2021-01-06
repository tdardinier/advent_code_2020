# cups = [4, 9, 6, 1, 3, 8, 5, 2, 7]
cups = [None for _ in range(10)]
cups[1] = [6, 3]
cups[2] = [5, 7]
cups[3] = [1, 8]
cups[4] = [7, 9]
cups[5] = [8, 2]
cups[6] = [9, 1]
cups[7] = [2, 4]
cups[8] = [3, 5]
cups[9] = [4, 6]
c = 4

def consistent(cups, i, n):
    done = set()
    c = i
    l = []
    while c not in done:
        l.append(c)
        done.add(c)
        c = cups[c][1]
    return c == i and n == len(l)



def to_list_from(cups, i):
    done = set()
    c = i
    l = []
    while c not in done:
        l.append(c)
        done.add(c)
        c = cups[c][1]
    return l



# Max of the list
N = 1000000

def check(cups):
    for i in range(1, N + 1):
        assert cups[cups[i][0]][1] == i
        assert cups[cups[i][1]][0] == i

def remove(cups, i):
    a = cups[i][0]
    b = cups[i][1]

    cups[a][1] = b
    cups[b][0] = a

def insert_after(cups, i, a):
    b = cups[a][1]
    cups[i] = [a, b]
    cups[a][1] = i
    cups[b][0] = i

def move(cups, current):
    picked_up = []
    c = current
    for _ in range(3):
        c = cups[c][1]
        picked_up.append(c)
    x = current - 1
    while x in picked_up:
        x -= 1
    if x == 0:
        x = N
        while x in picked_up:
            x -= 1
    remove(cups, picked_up[0])
    remove(cups, picked_up[1])
    remove(cups, picked_up[2])
    insert_after(cups, picked_up[0], x)
    insert_after(cups, picked_up[1], picked_up[0])
    insert_after(cups, picked_up[2], picked_up[1])
    return cups[current][1]

c = 7
for i in range(10, N + 1):
    cups.append([None, None])
    insert_after(cups, i, c)
    c = i

# check(cups)
c = 4
for i in range(10000000):
    c = move(cups, c)
a = cups[1][1]
b = cups[a][1]
print(a * b)

