# 백트래킹 - DFS + 가지치기
n, m = map(int, input().split())
visited = [False] * (n+1)
tmp = []

def DFS() :
    if len(tmp) == m :
        print(' '.join(map(str, tmp)))
        return 
    for i in range(1, n+1):
        if visited[i]  :
            continue
        visited[i] = True
        tmp.append(i)
        DFS()
        tmp.pop()
        visited[i] = False

DFS()





# for i in range(len(l)) : 
#     DFS(i, m)
