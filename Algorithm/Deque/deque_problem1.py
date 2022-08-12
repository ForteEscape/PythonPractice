from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
my_deque = deque(list(x for x in range(1, N + 1)))
key_list = list(map(int, sys.stdin.readline().split()))
ans = 0

for key in key_list:
    index = 0
    for x in range(len(my_deque)):
        if key == my_deque[x]:
            index = x
            break

    while my_deque[0] != key:
        if len(my_deque) - index > index:
            my_deque.rotate(-1)
            # my_deque.append(my_deque.popleft())
            ans += 1
        else:
            my_deque.rotate(1)
            # my_deque.appendleft(my_deque.pop())
            ans += 1

    my_deque.popleft()

print(ans)