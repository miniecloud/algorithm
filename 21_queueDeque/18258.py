from collections import deque
import sys 
input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    n = input().split()
    if n[0] == "push":
        q.append(n[1])
    if n[0] == "pop":
        if not q:
            print(-1)
        else : 
            print(q.popleft())
    if n[0] == "size":
        print(len(q))
    if n[0] == "empty":
        if not q:
            print(1)
        else :
            print(0)
    if n[0] == "front":
        if not q:
            print(-1)
        else :
            print(q[0])
    if n[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])

