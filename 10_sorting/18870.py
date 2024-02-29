# 문제를 이해 못함 ....
import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
d = {s:i for i, s in enumerate(sorted(set(l)))}
for i in l :  
    print(d[i], end=' ')
