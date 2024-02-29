n = int(input())
l = list(map(int, input().split()))
if n == 1:
    print(l[0]**2)
else :
    print(max(l)*min(l))

