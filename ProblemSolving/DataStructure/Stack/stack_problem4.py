# BOJ-17298 answer code
from collections import deque

seq_size = int(input())
seq = list(map(int, input().split()))

stack = deque()
ans = []

for x in reversed(seq):
    while stack and stack[-1] <= x:
        stack.pop()

    if not stack:
        ans.append(-1)
    else:
        ans.append(stack[-1])

    stack.append(x)

ans = reversed(ans)
print(*ans)