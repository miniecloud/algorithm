from collections import deque

N, K = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
answer = []

while dq:
    for _ in range(K-1) :
        dq.append(dq.popleft())
    answer.append(dq.popleft())



print('<',end='')
print(*answer, sep=', ', end='')
print('>',end='')
