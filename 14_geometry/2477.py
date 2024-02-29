n = int(input())
l = []
m, my= 0, 0
x_i, y_i =0, 0
for i in range(6):
    d, tmp = map(int, input().split())
    l.append([d, tmp])
    if d in [1,2] :
        if my < tmp :
            my = tmp
            y_i = (i + 3) % 6
    if d in [3, 4] :
        if m < tmp :
            m = tmp
            x_i = (i +3) % 6
print((m*my - l[x_i][1]*l[y_i][1])*n)
