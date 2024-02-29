n = int(input())

def star(i, n) :
    if 3//i == 3%i : 
        print(' ')
    else : 
        print('*')
     
    
for i in range(1, (n//3)+1) : 
    if i < n :
        star(i, n)  
    
