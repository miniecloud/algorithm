n = int(input())
l = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : (x[1], x[0]))
tmp = []
tmp.append(l[0])
for i in range(1, len(l)):
    if tmp[-1][1] <= l[i][0]:
        tmp.append(l[i])
print(len(tmp))    

