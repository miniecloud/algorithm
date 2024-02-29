n,m = map(int, input().split())
l = [input() for _ in range(n)]
cnt = 0
for _ in range(m) :
    w = input()
    if w in l :
        cnt += 1
print(cnt) 


