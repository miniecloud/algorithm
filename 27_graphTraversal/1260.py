import sys 
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, V = map(int, input().split())
g = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dfsResult = []
bfsResult = []
q = deque()

def dfs(V) :
    dfsResult.append(V)
    visited[V] = True
    for i in sorted(g[V]) :
        if not visited[i] :
            dfs(i)

def bfs(V):
    visited[V] = True
    q.append(V)
    while q:
        now = q.popleft()
        bfsResult.append(now)
        for i in sorted(g[now]) :
            if not visited[i]:
                visited[i] = True
                q.append(i)

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


dfs(V)
visited = [False] * (N+1)
bfs(V)
print(*dfsResult)
print(*bfsResult)


    
