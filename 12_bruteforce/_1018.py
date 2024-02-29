n, m = map(int, input().split())
l = [input() for _ in range(n)]
a = []
for i in range(n-7) :
    for j in range(m-7) :
        version1 = 0
        version2 = 0
        for k in range(i, i+8):
            for z in range(j, j+8):
                if (k+z) %2 == 0:
                    if l[k][z] != 'W':
                        version1 += 1
                    elif l[k][z] != 'B':
                        version2 += 1
                else :
                    if l[k][z] != 'B':
                        version1 += 1
                    elif l[k][z] != 'W':
                        version2 += 1
        a.append(version1)
        a.append(version2)
print(a)
print(min(a))
