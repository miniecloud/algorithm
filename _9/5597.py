import sys
l = [0] * 31

for _ in range(28):
    i = int(sys.stdin.readline())
    l[i] =1

for i in range(len(l)) :
    if i == 0 : continue
    if l[i] == 0:
        print(i)




