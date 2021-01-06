players = [[], []]
i = 0
for line in open("input.txt").readlines():
    if line[0] != "P":
        if line == "\n":
            i += 1
        else:
            players[i].append(int(line[:-1]))

def turn(players):
    if len(players[0]) > players[0][0] and len(players[1]) > players[1][0]:
        nplayers = [players[0][1:players[0][0] + 1], players[1][1:players[1][0] + 1]]
        g = play(nplayers)
    else:
        g = 1
        if players[0][0] > players[1][0]:
            g = 0

    players[g] = players[g][1:] + [players[g][0], players[1 - g][0]]
    players[1 - g] = players[1 - g][1:]

def play(players):

    played = []

    while len(players[0]) > 0 and len(players[1]) > 0:
        for game in played:
            if players[0] == game[0] and players[1] == game[1]:
                return 0
        played.append([[x for x in players[0]], [x for x in players[1]]])
        turn(players)

    g = 0
    if len(players[0]) == 0:
        g = 1
    return g

play(players)

n = len(players[g])
s = 0
for (i, c) in enumerate(players[g]):
    s += (n - i) * c
print(s)

