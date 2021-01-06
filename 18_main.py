def find_closing_parenthesis_index(s):
    n = 0
    for i in range(1, len(s)):
        if n == 0 and s[i] == ")":
            return i
        elif s[i] == "(":
            n += 1
        elif s[i] == ")":
            n -= 1

def iterate(s):
    if "(" in s:
        i = s.index("(")
        j = i + find_closing_parenthesis_index(s[i:])
        return "(" + s[:i] + iterate(s[i+1:j]) + s[j+1:] + ")"
    r = s.split(" ")
    a = int(r[0])
    if len(r) > 1:
        if r[1] == "+":
            a += int(r[2])
        elif r[1] == "*":
            a *= int(r[2])
        return "(" + (" ".join([str(a)] + r[3:])) + ")"
    else:
        return str(a)

def iterate2(s):
    print("iterate2", s)
    if "(" in s:
        i = s.index("(")
        j = i + find_closing_parenthesis_index(s[i:])
        return "(" + s[:i] + iterate2(s[i+1:j]) + s[j+1:] + ")"
    r = s.split(" ")
    if "+" in r:
        i = r.index("+")
        a = int(r[i-1]) + int(r[i+1])
        return "(" + " ".join(r[:i-1] + [str(a)] + r[i+2:]) + ")"
    a = int(r[0])
    if len(r) > 1:
        a *= int(r[2])
        return "(" + (" ".join([str(a)] + r[3:])) + ")"
    else:
        return str(a)

def evaluate(s, two=False):
    while " " in s:
        if two:
            s = iterate2(s)
        else:
            s = iterate(s)
    while s[0] == "(":
        s = s[1:-1]
    return int(s)

s = 0
for line in open("input.txt", "r").readlines():
    s += evaluate(line[:-1], True)
print(s)
