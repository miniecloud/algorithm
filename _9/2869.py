a, b, v = map(int, input().split())
if a > v :
    print('1')
else :
    v -= a
    q = int(v//(a-b))
    re = int(v%(a-b))
    if re :
        print(q+2)
    else : 
        print(q+1)



