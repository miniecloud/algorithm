import sys 
n, a = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for _ in range(n)]
test = max(l)+1

def check(x) :
    cnt = 0 
    for i in l :
        cnt += i//x
    return cnt

s = 1 # 후에 m이 0이 되면 런타임 에러가 날 수 있음...
e = test
ans = 0
while s<=e:
    m = (s+e)//2
    cnt = check(m)
    if cnt < a :
        e = m -1
    elif cnt >= a :
        s = m +1
        ans = m
print(ans)
