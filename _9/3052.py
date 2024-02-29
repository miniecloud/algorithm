import sys 
l = set([int(sys.stdin.readline())%42 for _ in range(10)])
print(len(l))
