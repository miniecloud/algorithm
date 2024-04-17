import sys 
input = sys.stdin.readline
n = int(input())
import time
s = time.time()
tmp = []
result = []
m = 0
check = True
for i in range(n) : 
    t = int(input())
    for j in range(m+1, t+1) :
        tmp.append(j)
        result.append("+")
    m = max(t, m)
    if tmp.pop() == t : 
        result.append('-')
    else:
        print("NO")
        check = False
        break

if check : 
    print(*result, sep="\n")
print(s-time.time())
