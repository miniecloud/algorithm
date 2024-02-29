import sys 
words = [list(input()) for _ in range(5)]

l = []
for i in range(15):
    for j in range(len(words)):
        if i > len(words[j])-1:
            continue
        l.append(words[j][i])

print(''.join(l))

