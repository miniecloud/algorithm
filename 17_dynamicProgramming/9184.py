l = [[[0]*21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 : 
        return 1

    if a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    if a < b and b < c :
        if l[a][b][c] == 0 :
            l[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return l[a][b][c] 

    else :
        if l[a][b][c] == 0 :
            l[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return l[a][b][c]


while True :
    a, b, c = map(int, input().split())
    if a == -1 and a == b and a == c:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')


