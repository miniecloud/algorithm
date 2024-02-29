n = int(input())
l = list(map(int, input().split()))
max_n = 0
dp = [0] * n

for i in range(len(l)):
    if i == 0 :
        dp[0] = l[0]
    dp[i] = max(dp[i-1]+l[i], l[i])

print(max(dp))



    
