(s1, s2) = (0, 0)
for l in open("input.txt", "r").readlines():
    ll = l[:-1].split(" ")
    lll = ll[0].split("-")
    (m, M, c, s) = (int(lll[0]), int(lll[1]), ll[1][0], ll[2])
    s1 += (m <= len([x for x in s if x == c]) <= M)
    s2 += ((s[m - 1] == c) ^ (s[M - 1] == c))
print(s1, s2)
