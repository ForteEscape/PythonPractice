from collections import deque

dataset = []
tc = 1
while True:
    data = input()
    if data[0] == '-':
        break

    stack = deque()
    for element in data:
        if element == "{":
            stack.append(element)
        else:
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(element)

    cnt = 0
    while stack:
        top = stack.pop()

        if stack[-1] == top:
            if top == '{':
                top = '}'
                cnt += 1
            else:
                tmp = stack.pop()
                tmp = '{'
                stack.append(tmp)
                cnt += 1
        else:
            tmp = stack.pop()
            tmp = '{'
            stack.append(tmp)
            cnt += 1

            top = '}'
            cnt += 1

        if stack and stack[-1] == '{':
            stack.pop()

    print("{}. {}".format(tc, cnt))
    tc += 1
