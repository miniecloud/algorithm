import sys
n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = []
for i in range(len(l)) :
    j = i-1
    k = i+1
    tmp = 1
    while j >= 0:
        if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
            tmp += 1 
        j -= 1
    while k <= n-1 :
        if l[i][0] < l[k][0] and l[i][1] < l[k][1]:
            tmp += 1 
        k += 1
    ans.append(tmp)
    
print(' '.join(map(str, ans)))
    



