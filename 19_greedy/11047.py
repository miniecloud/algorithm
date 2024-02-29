import sys
n, w = map(int, input().split())
l = [int(sys.stdin.readline()) for _ in range(n)]
cnt =0 

for i in range(len(l)-1, -1, -1):
    if w//l[i] > 0: 
        cnt += w// l[i]
        w = w%l[i]
print(cnt)

