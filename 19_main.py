rules = {}
words = []
past = False

# 0 = letter
# 1 = pair
# 2 = disjunction = pair of pair

for line in open("input.txt", "r").readlines():
    if line == "\n":
        past = True
    elif not past:
        r = line[:-1].split(": ")
        i = r[0]
        if '"' in r[1]:
            r = r[1].split('"')
            rules[i] = (0, r[1])
        elif " | " in r[1]:
            rr = r[1].split(" | ")
            rules[i] = (2, (rr[0].split(" "), rr[1].split(" ")))
        else:
            rules[i] = (1, r[1].split(" "))
    else:
        words.append(line[:-1])

def multiply(a, b):
    return [aa + bb for aa in a for bb in b]

def domain(rule):
    if rule[0] == 0:
        return [rule[1]]
    elif rule[0] == 1:
        l = [""]
        for i in rule[1]:
            l = multiply(l, domain(rules[i]))
        return l
    else:
        return domain((1, rule[1][0])) + domain((1, rule[1][1]))




def match(word, rule):
    if rule[0] == 0:
        return (word[0] == rule[1], word[1:])
    elif rule[0] == 1:
        (b, w) = (True, word)
        for i in rule[1]:
            (bb, w) = match(w, rules[i])
            b = b and bb
        return (b, w)
    else:
        (b, w) = match(word, (1, rule[1][0]))
        if b:
            return (b, w)
        else:
            return match(word, (1, rule[1][1]))

s = 0
for w in words:
    (b, ww) = match(w, rules["0"])
    s += (b and len(ww) == 0)
print(s)

A = set(domain(rules["42"]))
B = set(domain(rules["31"]))

n = 8
def matches(word):
    b = True
    ca = 0
    cb = 0
    i = 0
    while i * n < len(word):
        w = word[i*n:(i+1)*n]
        if w in A and cb == 0:
            ca += 1
        elif w in B:
            cb += 1
        else:
            b = False
        i += 1
    return b and (ca > cb) and cb > 0

s = 0
for w in words:
    s += matches(w)
print(s)
