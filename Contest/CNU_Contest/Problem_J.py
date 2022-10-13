import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
stock_list = list(map(int, sys.stdin.readline().split()))
ans = 0
stack = deque()

for element in stock_list:
    if not stack:
        stack.append(element)
    else:
        if element < stack[-1]:
            temp = stack[-1] - stack[0]

            if ans < temp:
                ans = temp

            while stack:
                stack.pop()
            stack.append(element)
        else:
            stack.append(element)

if stack:
    temp = stack[-1] - stack[0]
    if ans < temp:
        ans = temp

print(ans)
