import sys
from collections import Counter

n = int(sys.stdin.readline())
l = [int(sys.stdin.readline()) for _ in range(n)]

l_cnt =Counter(l)
m = max(l_cnt.values())
s_cnt = [(k, v) for k, v in l_cnt.items() if v==m] 
s_cnt = sorted(s_cnt, key=lambda x : x[0])
if len(s_cnt) >=2 :
    m = s_cnt[1][0]
else : 
    m = s_cnt[0][0]

print(round(sum(l)/n))
print(sorted(l)[n//2])
print(m)
print(max(l)-min(l))


