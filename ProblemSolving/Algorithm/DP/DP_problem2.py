import sys

N = int(sys.stdin.readline().rstrip())
weight = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
table = [[0 for _ in range(3)] for _ in range(N)]

R = []
G = []
B = []

for element in weight:
    R.append(element[0])
    G.append(element[1])
    B.append(element[2])

table[0][0] = R[0]
table[0][1] = G[0]
table[0][2] = B[0]

for i in range(1, N):
    table[i][0] = min(table[i - 1][1], table[i - 1][2]) + R[i]
    table[i][1] = min(table[i - 1][0], table[i - 1][2]) + G[i]
    table[i][2] = min(table[i - 1][0], table[i - 1][1]) + B[i]

print(min(table[N - 1]))
