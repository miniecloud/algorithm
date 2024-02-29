s = int(input())
e = int(input())
l = [i for i in range(s,e+1)]

for i in range(s, e+1):
    if i == 1: 
        l.remove(1)
        continue
    if i <= 3: continue
    for j in range(2, i//2+1):
        if i % j ==0 :
            print(i)
            l.remove(i)
            break

if len(l) == 0 :
    print(-1)
else: 
    print(sum(l))
    print(min(l))



        
