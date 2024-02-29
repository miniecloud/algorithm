n, m = map(int, input().split())
l = set(input() for _ in range(n))
l2 = set(input() for _ in range(m))
result = sorted(l&l2)
print(len(result))
# [print(i) for i in result]
print(*result, sep='\n')

