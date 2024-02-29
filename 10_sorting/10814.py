import sys
n = int(input())
l = [sys.stdin.readline().split() for _ in range(n)]
l = sorted(l, key = lambda x: int(x[0]))
[print(f'{i[0]} {i[1]}') for i in l]


