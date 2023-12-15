n = int(input())
currh = 0
langs = input().split()
organ, ha, hb = [0], [0], [0]
everyone = list(map(int,input().split()))
result = [0] * n
for i in everyone[1:len(everyone)-1]:
    if i == organ[-1]:
        if langs[i - 1] == 'A':
            temp = ha.pop()
            result[i - 1] = temp - ha[-1] -1
        else:
            temp = hb.pop()
            result[i - 1] = temp - hb[-1] - 1
        organ.pop()
        currh -= 1
    else:
        currh += 1
        if langs[i - 1] == 'A':
            ha.append(currh)
        else:
            hb.append(currh)
        organ.append(i)

print(*result)