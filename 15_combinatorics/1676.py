n = int(input())

def factorial(n) :
    if n == 0:
        return 1
    return n * factorial(n-1)

tmp = str(factorial(n))
cnt =0 
for i in range(len(tmp)-1, -1, -1):
    if tmp[i] != '0' :
        break
    cnt += 1
print(cnt)
    
