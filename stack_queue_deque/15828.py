from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dq = deque()

while True:
    n = int(input())
    if n == -1:
        break
    if n > 0 : 
        dq.append(n)
    if len(dq) > N : 
        while len(dq) > N :
            dq.pop()
    if n == 0:
        dq.popleft()

if dq :
    print(*dq, sep=' ')
else : 
    print("empty")

    
