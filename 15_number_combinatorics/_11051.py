n, k = map(int, input().split())
l = [[0]*(n+1) for _ in range(n+1)]
l[0][0] = 1
for i in range(1, n+1):
    for j in range(i+1):
        l[i][j] = l[i-1][j-1] + l[i-1][j]
print(l[n][k]%10007)
