n, k =map(int, input().split())
a = list(map(int, input().split()))
k_l = []
tmp = [0]*n

def merge_sort(a, p, r):
    if p<r :
        q = (p+r)//2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)

def merge(a, p, q, r):
    i = p
    j = q+1
    t = 0
    while i<=q and j<=r:
        if a[i] <= a[j]:
            k_l.append(a[i]) 
            tmp[t] = a[i]
            t += 1
            i += 1
        else :
            k_l.append(a[j]) 
            tmp[t] = a[j]
            t += 1
            j += 1
    while i<= q :
        k_l.append(a[i]) 
        tmp[t] = a[i]
        t += 1
        i += 1
    while j <= r :
        k_l.append(a[j]) 
        tmp[t] = a[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i<= r:
        a[i] = tmp[t]
        i += 1
        t += 1

merge_sort(a, 0, len(a)-1)

if len(k_l)+1 > k :
    print(k_l[k-1])
else :
    print(-1)

    


