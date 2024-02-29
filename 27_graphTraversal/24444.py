# bfs
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

def bfs(g, R):
    q.append(R)
    visited[R] = True
    global cnt
    while q : 
        search = q.popleft()
        cnt += 1
        seq[search-1] = cnt
        for i in sorted(g[search]):
            if not visited[i] : 
                q.append(i)
                visited[i] = True

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

bfs(g, R)
print(*seq, sep='\n')

