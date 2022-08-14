# BOJ 6198 answer code
from collections import deque

building = int(input())
stack = deque()
answer = 0

for x in range(building):
    height = int(input())

    while stack and stack[-1] <= height:
        stack.pop()

    answer += len(stack)
    stack.append(height)

print(answer)