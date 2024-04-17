import sys 
n = int(input())
l = []
for _ in range(n):
    w = sys.stdin.readline().split()
    o = w[0]
    if o == 'push' :
        l.append(int(w[1]))
    if o == 'top':
        if not l :
            print(-1)
        else :
            print(l[-1])
    if o == 'size' :
        print(len(l))
    if o == 'empty':
        if not l :
            print(1)
        else :
            print(0)
    if o == 'pop':
        if not l :
            print(-1)
        else :
            print(l.pop())

