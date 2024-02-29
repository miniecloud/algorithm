n = int(input())

for _ in range(n): 
    d = {}
    for _ in range(int(input())):
        i, t = input().split()
        if not t in d.keys():
            d[t] = 0
        d[t] +=1 
    cnt =  1 
    tmp = list(d.items())
    for j in range(len(tmp)):
        cnt *= (tmp[j][1] +1)
    print(cnt - 1)



    
