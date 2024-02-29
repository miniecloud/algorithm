l = [i for i in range(246913)]
l[1] =0

for i in range(2, int(len(l)**0.5)+1):
    if l[i] == 0 :
        continue
    for j in range(i+i, len(l), i):
        if l[i] == 0 :
            continue
        else : 
            l[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    tmp = list(set(l[n+1:(2*n)+1]))
    if 0 in tmp : 
        tmp.remove(0)
    print(len(tmp))
