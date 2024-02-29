n = int(input())

def star(i, j, n) :
    if ((i//3)%3 == 1 and (j//3)%3 ==1) :
        print(' ', end='')
    else :
        if n/3 == 0 :
            print('*', end='')
        else :
            star(i, j, n/3)

for i in range(0, n):
    for j in range(0,n) :
        star(i, j, n)
    print("")

