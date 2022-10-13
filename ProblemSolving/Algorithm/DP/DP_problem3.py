N = int(input())

table = [0 for _ in range(1001)]
mod = 10007

table[0] = 1
table[1] = 2

for i in range(2, N):
    table[i] = (table[i - 1] + table[i - 2]) % mod

print(table[N - 1])