from collections import deque

N = list(input())
stack = deque()
l = len(N)
is_in_bracket = False
ans = ''

for i in range(l):
    if N[i] == '<':
        is_in_bracket = True
        while stack:
            ans += stack.pop()

    if N[i] == ' ':
        while stack:
            ans += stack.pop()
        ans += N[i]
        continue

    if not is_in_bracket:
        stack.append(N[i])
    else:
        ans += N[i]

    if N[i] == '>':
        is_in_bracket = False

while stack:
    ans += stack.pop()

print(ans)