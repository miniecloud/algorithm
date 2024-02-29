S = list(input())
tmp = []
for i in range(1, len(S)+1):
    s = 0 
    e = i
    while e <= len(S):
        tmp.append(''.join(S[s:e]))
        s += 1
        e += 1
print(len(set(tmp)))
