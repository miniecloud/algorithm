import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
g = [[] for _ in range(N+1)]
visited = [False] * (N+1)
q = deque()
seq = [0] * (N)
global cnt
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

q.append(R)
visited[R] = True
while q : 
    search = q.popleft()
    cnt += 1
    seq[search-1] = cnt
    for i in sorted(g[search], reverse=True):
        if not visited[i] :
            q.append(i)
            visited[i] = True
print(*seq, sep="\n")
