n = int(input())
l = [int(input()) for _ in range(1, n+1)]

for i in range(n):  
    for j in range(0, n-i-1):
        if l[j] > l[j+1]:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
[print(i) for i in l]






