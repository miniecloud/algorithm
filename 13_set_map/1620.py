import sys
n, m = map(int, sys.stdin.readline().split())
d = dict()

for i in range(1, n+1):
    w = sys.stdin.readline().replace('\n','')
    d[w] = i
    d[i] = w
for _ in range(m) :
    q = sys.stdin.readline().replace('\n','')
    if q.isdigit() : 
        print(d[int(q)])
    else :
        print(d[q]) 



