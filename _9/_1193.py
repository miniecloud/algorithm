number = int(input())

tmp = number
for i in range(1,number+1) :     
    if i < tmp :
        tmp -= i
    else :
        if i%2 ==0:
            tmp -=1 
            s = i
            f = 1
            while tmp > 0 :
                tmp -= 1
                f += 1
                s -=1
        else : 
            tmp -= 1
            f = i
            s = 1
            while tmp > 0:
                tmp -= 1
                f -=1
                s += 1
        print(f'{f}/{s}')
        break











    


    

    

