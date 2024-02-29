n = int(input())

def factorial(n):
    ans=1
    if n > 0:
        ans = n * factorial(n-1)
        print(ans)
    return ans
    
print(factorial(n))
