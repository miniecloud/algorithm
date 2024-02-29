import sys
input = sys.stdin.readline
n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0] * (n) 
dp[0] = l[0]
if n >= 2: 
    dp[1] = l[0] + l[1] 
if n >= 3:
    dp[2] = max(l[1]+l[2], l[0] +l[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + l[i], dp[i-3]+l[i-1]+l[i] )

print(dp[n-1])
