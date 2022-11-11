N = int(input())

table = [0] * (N + 1)
table[1] = 1

if N >= 2:
    table[2] = 3

    for i in range(3, N + 1):
        table[i] = (table[i - 1] + table[i - 2] * 2) % 10007

print(table[N])