n, m, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cards = {}
for i in a:
    a_cards[i] = a_cards.get(i, 0) + 1

b_cards = {}
for i in b:
    b_cards[i] = b_cards.get(i, 0) + 1

res: int = 0
a = set(a).union(set(b))
for i in a:
    if i in a_cards:
        if i in b_cards:
            res += abs(a_cards[i] - b_cards[i])
        else:
            res += a_cards[i]
    else:
        res += b_cards[i]

ans = []

while q:
    type_p, player, card = input().split()
    type_p, card = int(type_p), int(card)
    a_cards.setdefault(card, 0)
    b_cards.setdefault(card, 0)
    res -= abs(a_cards[card] - b_cards[card])
    
    if player == 'A':
        a_cards[card] += type_p
    else:
        b_cards[card] += type_p
    
    res += abs(a_cards[card] - b_cards[card])
    ans.append(res)
    q -= 1
print(*ans)
