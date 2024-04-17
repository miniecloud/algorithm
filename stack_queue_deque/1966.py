from collections import deque

for _ in range(int(input())) :
    cnt, index = map(int, input().split())
    imp = deque(map(int, input().split()))
    dq = deque([i for i in range(1, cnt+1)])

    check = dq[index]
    count = 0
    while imp:
        if imp[0] < max(imp) :
            dq.append(dq.popleft())
            imp.append(imp.popleft())
        else : 
            count += 1
            if dq[0] == check :
                print(count)
                break
            dq.popleft()
            imp.popleft()



        




    
    
