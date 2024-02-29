import sys 
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l = sorted(l, key=lambda x:(x[1],x[0]))
[print(f'{i[0]} {i[1]}') for i in l]


