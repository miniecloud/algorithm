w = list(input().lower())
l = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
a = 0
for i in w:
    for j in l:
        if i in j :
            a += (l.index(j)+3)
print(a)
