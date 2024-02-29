n, m = map(int, input().split())
l = set(map(int, input().split()))
l2 = set(map(int, input().split()))
print(len((l-l2)|(l2-l)))
