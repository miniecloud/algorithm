from collections import deque

N, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
pull = list(map(int, input().split()))
cnt = 0 

for p in pull :
    m = len(dq)//2
    while True:
        if dq[0] == p :
            dq.popleft()
            break
        else : 
            if dq.index(p) > m :
                dq.appendleft(dq.pop())
                cnt += 1
            else : 
                dq.append(dq.popleft())
                cnt +=1 
print(cnt)
        


