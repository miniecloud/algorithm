while True:
    l = list(map(int, input().split()))
    if max(l)==0:
        break
    m = max(l)
    l.remove(m)
    if l[0]**2 + l[1]**2 == m**2:
        print('right')
    else :
        print("wrong")


