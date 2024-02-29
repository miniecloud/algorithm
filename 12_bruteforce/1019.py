n, m = map(int, input().split())
l = [list(input()) for _ in range(n)]

c1 = [[0]*m for _ in range(n)]
c2 = [[0]*m for _ in range(n)]

for a in range(n - 7):
    for b in range(m-7) :

        for i in range(n+8) :
            for j in range(m+8) :
                if l[i][j] != l[i][j+1]:
                    continue
                if l[i][j] == 'W' :
                    l[i][j+1]  = 'B'
                    c[i][j+1] = 1
                if l[i][j] == 'B' :
                    l[i][j+1]  = 'W'
                    c[i][j+1] = 1
