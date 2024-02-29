import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
p = [0] * (n-m+1)

for i in range(n-m+1):
    if i == 0 : 
        p[0] = sum(l[:m])
    else :
        p[i] = p[i-1] - l[i-1] + l[i+m-1]
print(max(p))
    
    

