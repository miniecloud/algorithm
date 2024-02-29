n = int(input())

for _ in range(n):
    tmp = list(input())
    stack = []
    for i in range(len(tmp)):
        if tmp[i] == '(':
            stack.append(tmp[i])
        elif tmp[i] == ')':
            if len(stack) == 0 :
                print("NO")
                break
            else : 
                stack.pop()
        if i == len(tmp)-1 :
            if not stack :
                print("YES")
            else :
                print("NO")

