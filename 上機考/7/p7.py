with open("7/data.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    d, g = [[0]], [0] * (n + 1)
    for i in range(1, n + 1):
        d.append(file.readline().strip())
        for j in range(m):
            g[i] += 1 << j if d[i][j] == 'H' else 0

# 計算x中有多少個1
def count(x):
    res = 0
    while x:
        x &= x - 1
        res += 1
    return res

# 判斷第x行中j狀態是否合法 
def check(j, x):
    return (j & (j >> 1)) == 0 and (j & (j >> 2)) == 0 and j & g[x] == 0

# 1. 預處理出對每一行來說合法的狀態和其中有多少個1
st = [[0] for i in range(n + 2)]
cnt = [0] * (1 << m)
maxm = 0
for i in range(1, n + 1):
    for j in range(1, 1 << m):
        if check(j, i):
            st[i].append(j)
            cnt[j] = count(j)
    maxm = max(maxm, len(st[i]))

# 2. 狀態轉移
dp = [[[0 for k in range(1 << m)] for j in range(1 << m)] for i in range(n + 2)]
# 2.1 先處理第1行，此時只需要考慮自身即可
for a in st[1]:
    dp[1][a][0] = cnt[a]
# 2.2 從第2行開始枚舉
for i in range(2, n + 2): # 當前在第i行
    for a in st[i]:  # 第i行的所有合法狀態a
        for b in st[i - 1]: # 第i-1行的所有合法狀態b
            for c in st[i - 2]: # 第i-2行的所有合法狀態c
                if a & b == 0 and b & c == 0 and a & c == 0:  # 三行不能相交
                    dp[i][a][b] = max(dp[i][a][b], dp[i - 1][b][c] + cnt[a])
print(max(dp[n + 1][0]))
