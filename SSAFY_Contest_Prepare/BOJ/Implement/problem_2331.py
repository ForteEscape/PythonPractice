N, P = map(int, input().split())
seq = {N: 1}

data = N
while True:
    tmp = 0
    while data != 0:
        tmp += (data % 10) ** P
        data //= 10

    if tmp not in seq:
        seq[tmp] = 1
    else:
        seq[tmp] += 1

    if seq[tmp] >= 3:
        break

    data = tmp

ans = []
for keys in seq:
    if seq[keys] < 2:
        ans.append(keys)

print(len(ans))