while True:
    s = input()
    stack = []
    if len(s) == 1 and s=="." :
        break
    s = list(i for i in list(s) if "(" in i or ")" in i or "[" in i or "]" in i)
    if not s :
        print("yes")
        continue

    check = True
    for i in range(len(s)) :
        if s[i] == "(" or s[i] == "[":
            stack.append(s[i])
        elif s[i] == ")" or s[i] == "]":
            if not stack : 
                check = False
                break
            else : 
                tmp = stack.pop()
                if s[i] == ")":
                    if tmp != "(":
                        check = False
                        break
                if s[i] == "]":
                    if tmp != "[":
                        check = False
                        break
    if check : 
        if not stack : 
            print("yes")
        else :
            print("no")
    else : 
        print("no")


