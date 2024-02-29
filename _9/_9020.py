import sys
n = int(sys.stdin.readline())
s = [0] * 10001

s[1] = 1
for i in range(2, int(10001**0.5)+1):
    for j in range(i+i, 10001, i) :
        s[j] = 1
 
for _ in range(n):
    tmp = int(sys.stdin.readline())
    l = []
    c = True
    a = []
    for i in range(tmp+1):
        if s[i] == 0 :
            l.append(i)

    for i in range(len(l)//2, len(l)):
        c = False
        for j in range(i, -1, -1) : 
            if l[i] + l[j] == tmp:
                print(f'{l[j]} {l[i]}')
                c = True
                break
            elif l[i] + l[j] > tmp:
                continue
            elif l[i] + l[j] < tmp:
                break
        if c:
            break
        
