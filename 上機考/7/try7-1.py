with open("7/data.txt","r") as file:
    n, m = map(int, file.readline().split())
    d, g = [[0]], [0]*(n+1)
    for i in range(1, n+1):
        d.append(file.readline().strip())
        for j in range(m):
            g[i] += 1 << j if d[i][j] == 'H' else 0

def count(x):
    fake = 0
    while x:
        x &= x-1
        fake += 1
    return fake

def check(j,x):
    return (j & (j>>1)) == 0 and (j & (j>>2)) == 0 and j & g[x] == 0

st = [[0] for i in range(n+2)]
cnt = [0]*(1<<m)
maxm = 0
for i in range(1, n+1):
    for j in range(1, 1<<m):
        if check(j,i):
            st[i].append(j)
            cnt[j] = count(j)
    maxm = max(maxm, len(st[i]))

dp = [[[0 for k in range(1<<m)] for j in range(1<<m)] for i in range(n+2)]
for a in st[1]:
    dp[1][a][0] = cnt[a]
for i in range(2,n+2):
    for a in st[i]:
        for b in st[i-1]:
            for c in st[i-2]:
                if a & b == 0 and b & c == 0 and a & c == 0:
                    dp[i][a][b] = max(dp[i][a][b], dp[i-1][b][c]+cnt[a])
print(max(dp[n+1][0]))