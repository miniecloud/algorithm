n = input().split('-')
tmp = []
for i in n:
    tmp.append(sum(map(int, i.split('+'))))
result = tmp[0]
for i in range(len(tmp)):
    if i==0:continue
    result -= tmp[i]
print(result)
 
