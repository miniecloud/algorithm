n = str(input())
alpha = ['c=', 'c-', 'dz=', 'd-','lj','nj','s=','z=']

for i in alpha :
    n = n.replace(i, '1')
print(len(list(n)))
