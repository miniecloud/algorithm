n = int(input())
l = []

for _ in range(n) :
    tmp = int(input())
    if tmp == 0 :
        l.pop()
    else :
        l.append(tmp)
        
print(sum(l))
