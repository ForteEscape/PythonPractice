# BOJ 17608 answer code
from collections import deque

tc = int(input())
stack = deque()

for x in range(tc):
    height = int(input())

    while stack and stack[-1] <= height:
        stack.pop()

    stack.append(height)

print(len(stack))