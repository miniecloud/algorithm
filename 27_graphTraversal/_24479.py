# 출력을 잘못 이해함...
# 재귀 값 계산 잘못함.. 값을 넘겨받을 경우 안에 변수도 메모리에 저장됨.. 
import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]
visited = [False]*(N+1)
check = [0] * N
global cnt
cnt = 1 

def dfs(g, R) :
    global cnt
    check[R-1] = cnt
    cnt += 1

    visited[R] = True
    for i in sorted(g[R]) :
        if not visited[i] :
            dfs(g, i)

for _ in range(M) :
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)


dfs(g, R)
print(*check, sep='\n')


    
