import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
b_score = list(map(int, sys.stdin.readline().split()))
b_sequence = list(map(int, sys.stdin.readline().split()))
blowed = [False for _ in range(N)]
max_score = -1e9
section = []

# prefix sum
sum_value = 0
prefix_sum = [0]
for i in b_score:
    sum_value += i
    prefix_sum.append(sum_value)

epoch = 0
while epoch < N:
    blowed[b_sequence[epoch] - 1] = True
    epoch += 1

    section.append(b_sequence[epoch] - 1)

