number = int(input())

ans =0
for _ in range(number):
    k = int(input())
    n = int(input())
    l = [[i for i in range(n+1)]]

    for i in range(1, k+1) :
        tmp = []
        for j in range(n+1) :
            tmp.append(sum(l[i-1][:j+1]))
        l.append(tmp)

    print(l[k-1][n]+ l[k][n-1])

        








