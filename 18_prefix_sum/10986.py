from itertools import accumulate
n, m = map(int, input().split())
l = list(map(int, input().split()))
a = [0] * (len(l)+1)
cnt = 0

for i in range(1,len(l)+1):
    a[i] = (a[i-1] + l[i-1])%m
print(a)
    
for i in range(m):
    cnt += a[i] * (a[i]-1)/2
print(cnt)
# for i in range(n):
#     m = a[i]
#     for j in range(i+1, n):
#         if (a[j]-m)%3 == 0:
#             cnt +=1 
print(cnt)
    # for j in range(i, 5):
    #     if i == 0 :
    #         a[i][j] = a[i][j-1] + l[j]
    #         if a[i][j] % 3 == 0 :
    #             cnt += 1
    #     else :
    #         a[i][j] = a[i][j-1] + l[j]
    #         if a[i][j] % 3 == 0 :
    #             cnt += 1



