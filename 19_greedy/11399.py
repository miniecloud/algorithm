n = int(input())
l = sorted(map(int, input().split()))
tmp = [0]*n
for i in range(len(l)):
    tmp[i] = tmp[i-1] + l[i] 
print(sum(tmp))

