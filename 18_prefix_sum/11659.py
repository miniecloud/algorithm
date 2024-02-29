import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
p = [0]* (n+1)

for i in range(n) :
    p[i+1] = p[i] + l[i]
    
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(p[e]-p[s-1])
