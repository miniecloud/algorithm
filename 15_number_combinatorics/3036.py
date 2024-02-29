import math
n = int(input())
l = list(map(int, input().split()))

for i in range(1,len(l)):
    f = l[0]
    gcd = math.gcd(f, l[i])
    print(f'{f//gcd}/{l[i]//gcd}')



