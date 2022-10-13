import sys

N = int(sys.stdin.readline().rstrip())
consult_data = [[] for _ in range(N)]
table = [0 for _ in range(20)]

for i in range(N):
    time, price = map(int, sys.stdin.readline().split())
    consult_data[i].append(time)
    consult_data[i].append(price)

for i in range(N - 1, -1, -1):
    if consult_data[i][0] + i > N:
        table[i] = table[i + 1]
    else:
        table[i] = max(consult_data[i][1] + table[i + consult_data[i][0]], table[i + 1])

print(table[0])