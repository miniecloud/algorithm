nunber = int(input())

for _ in range(nunber):
    h, w, n = map(int, input().split())

    if n%h < 1 :
        ans_n = n//h 
        ans_h = h
    else :
        ans_n = n//h +1
        ans_h = int(n%h)

    ans = str(ans_h) + str(ans_n).zfill(2)
    print(ans)

