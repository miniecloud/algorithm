import sys 
input = sys.stdin.readline
N = int(input())
s = []
visited = [[0] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
cnt = 1 
result = []

for _ in range(N) :
    s.append(list(map(int, input().rstrip())))


def dfs(x, y):
    visited[x][y] = cnt
    result[cnt-1] += 1
    i = 0
    while i < 4:
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        i += 1 
        if tmp_x < 0 or tmp_y < 0 or tmp_x == N or tmp_y==N:
            continue
        if s[tmp_x][tmp_y] == 1 and visited[tmp_x][tmp_y] == 0:
            visited[tmp_x][tmp_y] = cnt
            dfs(tmp_x, tmp_y)

for i in range(N) :
    for j in range(N):
        if s[i][j] == 1 and visited[i][j] == 0:
            result.append(0)
            dfs(i, j)
            cnt +=1 

print(len(result))
print(*sorted(result), sep="\n")
