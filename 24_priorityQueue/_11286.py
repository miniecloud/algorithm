import sys 
import heapq
input = sys.stdin.readline

l = []
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        if not l:
            print(0)
        else : 
            print(heapq.heappop(l)[1])
    else :
        heapq.heappush(l, (abs(n), n))


