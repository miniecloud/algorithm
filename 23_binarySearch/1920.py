n = int(input())
l = list(map(int, input().split())) 
m = int(input())
c = list(map(int, input().split())) 

l.sort()
for i in range(m):
    ans = 0
    check = c[i]
    s = 0
    e = len(l)-1
    while s<=e:
        m = (s+e)//2
        if check == l[m] :
            ans = 1
            break
        elif check < l[m] :
            e = m -1
        elif check > l[m] :
            s = m + 1
    print(ans)
        



    
