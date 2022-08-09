# BOJ 4949 answer code
from collections import deque

while True:
    stack = deque()
    data = input()
    balanced = True

    if data == '.':
        break

    for index in data:
        if index in ['(', '[']:
            stack.append(index)
        elif index in [')', ']']:
            if not stack:
                balanced = False
                break

            if (stack[-1] == '[' and index == ']') or (stack[-1] == '(' and index == ')'):
                stack.pop()
            else:
                balanced = False
                break

    if stack:
        balanced = False

    if balanced:
        print("yes")
    else:
        print("no")
