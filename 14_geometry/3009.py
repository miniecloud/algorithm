x, y = [], []
a = []
for _ in range(3):
    s, e = map(int, input().split())
    x.append(s)
    y.append(e)
for i in x :
    if x.count(i) == 1:
        a.append(i)
        break
for i in y :
    if y.count(i) == 1:
        a.append(i)
        break
print(f'{a[0]} {a[1]}')
 
# xor 로 매우간단하게 풀 수 있음 
# xor 은 자기자신과 하면 0이 나옴
#        0과 하면 자기자신이 나옴
            

        


