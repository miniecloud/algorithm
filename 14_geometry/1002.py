n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    tmp_x= max(x1, x2) - min(x1, x2)
    tmp_y= max(y1, y2) - min(y1, y2)
    tmp_len = (tmp_x**2 + tmp_y**2)**0.5
    if tmp_len == 0 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    elif max(r1, r2)-min(r1, r2) > tmp_len :
        print(0)
    elif max(r1, r2)-min(r1, r2) == tmp_len :
        print(1) 
    else :
        if r1+r2 > tmp_len :
            print(2)
        elif r1+ r2 == tmp_len:
            print(1)
        else :
            print(0)
        

