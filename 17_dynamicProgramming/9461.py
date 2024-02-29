n = int(input())
p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
[p.append(0) for _ in range(100)]

for _ in range(n) :
    k = int(input())
    for i in range(k+1):
        if p[i] != 0 :
            if i == k+1 : 
                print(p[i])
            continue
        p[i] = p[i-1] + p[i-5]
    print(p[k])
    


    

