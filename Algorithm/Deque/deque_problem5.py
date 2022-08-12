from collections import deque
import sys

N, K, M = map(int, sys.stdin.readline().split())
direction = 0
cnt = 0

my_deque = deque([x for x in range(1, N + 1)])
while my_deque:
    if direction == 0:
        my_deque.rotate(-(K - 1))
    else:
        my_deque.rotate(K)

    print(my_deque.popleft())
    cnt += 1

    if cnt == M:
        cnt = 0
        if direction == 0:
            direction = 1
        else:
            direction = 0
