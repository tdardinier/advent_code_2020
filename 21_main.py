food = {}
aller = {}
lines = []
for line in open("input.txt").readlines():
    r = line[:-2].split(" (contains ")
    allergens = set(r[1].split(", "))
    ingredients = set(r[0].split(" "))
    lines.append((ingredients, allergens))
    for f in ingredients:
        if f not in food:
            food[f] = allergens
        else:
            food[f] = food[f].union(allergens)
    for a in allergens:
        if a not in aller:
            aller[a] = ingredients
        else:
            aller[a] = aller[a].intersection(ingredients)

c = 0
solution = {}
for (i, _) in lines:
    for ii in i:
        b = False
        for a in aller:
            b = b or ii in aller[a]
        if not b:
            c += 1
        else:
            solution[ii] = None

def backtrack(solution, remaining_ingre):
    print("backtrack", solution, remaining_ingre)
    if len(remaining_ingre) == 0:
        return (True, solution)
    else:
        i = remaining_ingre[0]
        for a in aller[i]:
            if solution[a] is None:
                solution[a] = i
                (b, ss) = backtrack(solution, remaining_ingre[1:])
                if b:
                    return (b, ss)
                else:
                    solution[a] = None
    return (False, None)

l = []
for i in aller:
    l.append(i)
(b, s) = backtrack(solution, l)
print(s)

ll = list(solution.keys())
ll.sort(key = lambda x: solution[x])
