# from collections import Counter
# n = int(input())
# cnt = n
# for _ in range(n):
#     w = list(input())
#     d = Counter(w)
#     for k, v in d.items():
#         if v == 1 :
#             continue
#         else : 
#             c = ''.join(w).index(str(k))   
#             cv = v-1
#             i = 1
#             while c+i < len(w) and w[c] == w[c+i]:
#                 cv -=1 
#                 i +=1 
#             if cv > 0 :
#                 cnt -= 1
#                 break
# print(cnt)  

# v2
n = int(input())
for _ in range(n):
    w = input()
    print(w)
    print(sorted(w, key=w.find))
    if list(w) != sorted(w, key=w.find):
        n-=1
print(n)
