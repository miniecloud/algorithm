n = int(input())
l = [[0]*101 for _ in range(101)]

for _ in range(n) :
    a, b = map(int, input().split())
    for i in range(a, a+10) :
        for j in range(b, b+10) :
            l[i][j] = 1

cnt = 0
for i in range(len(l)):
    cnt += l[i].count(1)
    
print(cnt)

#문제 감을 잘못잡음






