k = int(input())

ans = 0
while k>= 0 :
    if 0< k < 3 :
        print(-1)
        break
    if k % 5 == 0:
        ans += k//5
        print(ans)
        break
    k -= 3
    ans += 1






