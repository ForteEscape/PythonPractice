# BOJ 2161 answer code
from collections import deque

card = int(input())
queue = deque()
ans = []

for x in range(1, card + 1):
    queue.append(x)

while len(queue) != 1:
    ans.append(queue[0])
    queue.popleft()
    queue.rotate(-1)

ans.append(queue[0])
print(*ans)