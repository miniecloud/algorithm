n, m = map(int, input().split())
visited = [False] * (n+1)
tmp = []

def DFS() :
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return 
    for i in range(1, n+1) :     
        if tmp and tmp[-1] > i :
            continue
        visited[i] = True
        tmp.append(i)
        visited[i] = False
        DFS()
        tmp.pop() 

DFS()
