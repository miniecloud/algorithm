import sys 
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    command = deque(input().rstrip())
    length = int(input())
    tmp = input().rstrip().replace("[","").replace("]","")
    e = True
    check = True

    if tmp == '' :
        dq = deque()
    else :
        dq = deque(map(int, tmp.split(",")))

    while command :
        c = command.popleft()
        if c == 'R' :
            check = not check
        else :
            if dq :
                if not check :
                    dq.pop()
                else:
                    dq .popleft()
            else :
                e = False
                break

    if not check : 
        dq = deque(list(dq)[::-1])

    if not e :
        print("error")
    else:
        print('['+','.join(map(str, list(dq)))+']')

