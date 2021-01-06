def iterate(sn, v):
    return (v * sn) % 20201227

(a, b) = (13135480, 8821721)
(v, n) = (1, 0)

while v != a:
    v = iterate(7, v)
    n += 1

v = 1
for _ in range(n):
    v = iterate(b, v)

print(v)
