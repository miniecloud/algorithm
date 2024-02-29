import sys 
n = int(sys.stdin.readline())
l = [input() for _ in range(n)]
l = sorted(set(l), key=lambda x:(len(x), ascii(x)))
[print(i) for i in l]

         
