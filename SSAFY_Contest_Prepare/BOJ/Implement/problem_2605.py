from collections import deque

N = int(input())
data = list(map(int, input().split()))
stack = deque()

idx = 1
for i in range(N):
    if data[i] == 0:
        stack.append(idx)
        idx += 1
        continue

    tmp_stack = deque()
    for j in range(data[i]):
        tmp_stack.append(stack.pop())

    stack.append(idx)
    while tmp_stack:
        stack.append(tmp_stack.pop())
    idx += 1

print(*stack)
