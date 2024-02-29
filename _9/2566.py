l = [list(map(int, input().split())) for _ in range(9)]

# -1 때문에.....
m = -1 
m_i = 0
n_i = 0 
for i in range(9):
    tmp = max(l[i])
    if tmp > m :
        m = tmp
        m_i = i +1
        n_i = l[i].index(m) + 1
print(m)
print(f'{m_i} {n_i}')

        
