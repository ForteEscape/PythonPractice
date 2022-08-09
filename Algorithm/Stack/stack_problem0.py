# BOJ 9012 answer code
from collections import deque

tc = int(input())

for x in range(tc):
    vps = input()
    flag = False
    stack = deque()

    for element in vps:
        if element == '(':
            stack.append(element)
        elif element == ')':
            if not stack:
                flag = True
                break
            else:
                stack.pop()

    if flag:
        print("NO")
        continue

    if not stack:
        print("YES")
    else:
        print("NO")