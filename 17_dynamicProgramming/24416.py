# 재귀 vs 동적계획법
n = int(input())
r = 0 
dp = 0

def fib_recursion(n) :
    global r
    if n== 1 or n== 2:
        r += 1
        return 1
    else :
        return fib_recursion(n-1) + fib_recursion(n-2)

f = [0] * (n+1)
def fib_dp(n):
    global dp
    if n == 1 or n == 2 :
        f[1] = 1
        f[2] = 1
    for i in range(3, n+1):
        dp += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib_recursion(n)
fib_dp(n)
print(r, dp)
