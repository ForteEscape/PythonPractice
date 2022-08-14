# BOJ 10773 answer code
from collections import deque

k = int(input())
stack = deque()

for x in range(k):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(list(stack)))
