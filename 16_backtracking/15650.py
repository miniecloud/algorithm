n, m = map(int, input().split())
visited = [False] * (n+1)
tmp = []

def dfs() :
    if len(tmp) == m :
        print(' '.join(map(str, tmp)))
        return  
    for i in range(1, n+1) :
        if visited[i] :
            continue
        if not tmp:
            visited[i] = True
            tmp.append(i)
        else :
            if tmp[-1] < i:
                visited[i] = True
                tmp.append(i)
            else : continue
        dfs()  
        tmp.pop()
        visited[i] = False

dfs()
