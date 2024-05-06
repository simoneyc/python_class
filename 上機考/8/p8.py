N = 50010
f = list(range(N))
d = [0] * N

def find(x):
    if f[x] != x:
        t = find(f[x])
        d[x] += d[f[x]]
        f[x] = t
    return f[x]

res = 0

with open('8/data.txt', 'r') as file:
    n, k = map(int, file.readline().split())
    for _ in range(k):
        t, x, y = map(int, file.readline().split())
        if x > n or y > n:
            res += 1
        else:
            px = find(x)
            py = find(y)
            if t == 1:
                if px == py and (d[x] - d[y]) % 3:
                    res += 1
                elif px != py:
                    f[px] = py
                    d[px] = d[y] - d[x]
            else:
                if px == py and (d[x] - d[y] - 1) % 3:
                    res += 1
                elif px != py:
                    f[px] = py
                    d[px] = d[y] - d[x] + 1

print(res)
