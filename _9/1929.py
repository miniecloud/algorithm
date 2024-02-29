m, n =map(int,input().split())

def fac(n) :
    if n ==1 :
        return False 
    if n <= 3 :
        return n
    else:
        for i in range(2, int(n**0.5)+1): 
            if n % i ==0:
                return False
    return n

for i in range(m, n+1):
    check = fac(i)
    if check :
        print(i)
