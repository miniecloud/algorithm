import sys
input = sys.stdin.readline
w = input().replace('\n','')
n = int(input())
# l = [[0]*26 for _ in range(len(w)+1)]
l = [[0]*26]

for i in range(1,len(w)+1) : 
    tmp = list()
    tmp += l[i-1]
    tmp[ord(w[i-1])-97] +=1
    l.append(tmp)

for i in range(n):
    c, s, e = input().rstrip().split()
    s, e =  int(s), int(e)
    col = ord(c)-ord('a')
    sys.stdout.write(f'{l[e+1][col] - l[s][col]}\n')

