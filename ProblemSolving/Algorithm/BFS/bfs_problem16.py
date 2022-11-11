import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())
queue = deque()
queue.append([A, 1])

while queue:
    cn, t = queue.popleft()

    if cn > B:
        continue

    if cn == B:
        print(t)
        break

    queue.append([cn * 2, t + 1])
    queue.append([cn * 10 + 1, t + 1])
else:
    print(-1)