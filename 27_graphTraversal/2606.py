import sys
from collections import deque
input = sys.stdin.readline
cnt = int(input())
c = int(input())
g = [[] for _ in range(cnt+1)]
visited = [0] * (cnt+1)
q = deque()

for _ in range(c) :
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

q.append(1)
visited[1] = 1

while q :
    now = q.popleft()
    for i in g[now] :
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

print(sum(visited)-1)


