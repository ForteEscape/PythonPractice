# BOJ 6198 answer code
from collections import deque

n = int(input())
data = list(map(int, input().split()))

print(data)

stack = deque()
stack.append([100000001, 0])
index = 1
ans = []

for element in data:
    while stack[-1][0] <= element:  # stack의 top이 element보다 작은 동안
        stack.pop()

    ans.append(stack[-1][1])
    stack.append([element, index])
    index += 1

print(*ans)