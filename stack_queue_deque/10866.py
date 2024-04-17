from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
for _ in range(int(input())):
    tmp = input().split(' ')
    c = tmp[0].replace('\n','')
    if c == "push_front" :
        dq.appendleft(int(tmp[1].replace(" ","")))
    if c == "push_back":
        dq.append(int(tmp[1].replace(" ","")))
    if c == "pop_front": 
        if dq :
            print(dq.popleft())
        else :
            print(-1)
    if c == "pop_back": 
        if dq : 
            print(dq.pop())
        else :
            print(-1)
    if c == "size":
        print(len(dq))
    if c == "empty" :
        if dq :
            print(0)
        else :
            print(1)
    if c == "front" :
        if dq :
            print(dq[0])
        else :
            print(-1)
    if c == "back":
        if dq :
            print(dq[-1])
        else :
            print(-1)


