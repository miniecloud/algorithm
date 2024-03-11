n = int(input())

def count(n):
    if n == 0 :
        return 1
    return n*count(n-1)

for _ in range(n):
    w, e = map(int, input().split())
    print(count(e)//(count(e-w)*count(w)) )

