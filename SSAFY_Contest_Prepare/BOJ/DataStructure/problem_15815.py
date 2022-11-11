from collections import deque

data = list(input())
stack = deque()

for i in range(len(data)):
    if data[i] not in ['+', '*', '-', '/']:
        stack.append(data[i])
    else:
        oper1 = int(stack[-1])
        stack.pop()

        if data[i] == '+':
            result = oper1 + int(stack[-1])
        elif data[i] == '*':
            result = oper1 * int(stack[-1])
        elif data[i] == '-':
            result = int(stack[-1]) - oper1
        else:
            result = int(stack[-1]) // oper1

        stack.pop()
        stack.append(result)

print(stack[-1])
