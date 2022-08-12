from collections import deque
import sys

N = int(sys.stdin.readline())
my_deque = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while my_deque:
    idx, paper = my_deque.popleft()
    ans.append(idx + 1)

    if paper > 0:
        my_deque.rotate(-(paper - 1))
    else:
        my_deque.rotate(-paper)

print(*ans)



