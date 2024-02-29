import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
g = [[] for _ in range(N+1)]
visited = [False] *(N+1)
visited_seq = [0] * (N)
cnt = 1

def dfs(g, R):
    global cnt
    visited_seq[R-1] = cnt
    cnt += 1
    visited[R] = True
    for i in g[R] :
        if not visited[i] :
            dfs(g, i)

for _ in range(M) :
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

g = [sorted(l, reverse=True) for l in g]

dfs(g, R)
print(*visited_seq, sep='\n')
