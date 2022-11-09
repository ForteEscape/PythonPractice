N = int(input())
wine = []

# table[i] = i번째 와인잔 까지의 최적의 해
# wine[i] = i번째 와인잔에 있는 와인의 양
table = [0] * (N + 1)

for i in range(N):
    amount = int(input())
    wine.append(amount)

table[0] = wine[0]
if N > 1:
    table[1] = wine[0] + wine[1]

    for i in range(2, N):
        table[i] = max(table[i - 1], table[i - 3] + wine[i - 1] + wine[i], table[i - 2] + wine[i])

print(table[N - 1])