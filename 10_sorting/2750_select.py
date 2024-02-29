# O(n**2)
import sys
n = int(input())
l = [int(input()) for _ in range(1, n+1)]

for i in range(n-1):
    m = sys.maxsize
    m_i = 0
    for j in range(i, n):
        if m > l[j] :
            m = l[j]
            m_i = j
    tmp = l[i]
    l[i] = l[m_i]
    l[m_i] = tmp
    print(l)





