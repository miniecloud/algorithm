n = int(input())
ans =0
for i in range(1, n):
    tmp = i + sum(map(int, list(str(i))))
    if tmp == n:
        ans = i
        break
    
print(ans)
