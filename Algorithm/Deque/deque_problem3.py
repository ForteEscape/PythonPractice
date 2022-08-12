from collections import deque
import sys

N, L = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
my_deque = deque()
ans = []

for x in range(N):

    while my_deque and my_deque[-1][0] >= data[x]:
        my_deque.pop()

    my_deque.append([data[x], x])

    if my_deque[0][1] < (x - L + 1):
        my_deque.popleft()

    ans.append(my_deque[0][0])

print(*ans)
