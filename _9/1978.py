n = int(input())
l = list(map(int, input().split()))

for i in range(n):
    num = l[i]
    if num == 1 : 
        l[i] = 0
    for j in range(2, num):
        if num % j == 0 :
            l[i] = 0
            break

cnt = 0 
for i in l :
    if i == 0 :
        continue
    cnt +=1
print(cnt)




