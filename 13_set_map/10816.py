from collections import Counter
n, card = int(input()), list(map(int, input().split()))
m, check = int(input()), list(map(int, input().split()))
ans = []
card.sort()
card_dict = Counter(card)

for i in check :
    tmp =0
    s = 0
    e = n-1

    while s <= e :
        m = (s+e)//2
        if card[m] == i :
            tmp = card_dict[i]
            break
        elif card[m] < i :
            s = m+1
        else :
            e = m-1
    ans.append(tmp)
            
print(' '.join(map(str, ans)))
