# learn about prefix sum technic
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
table = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    table[i] = table[i - 1] + num_list[i - 1]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(table[end] - table[start - 1])
