from collections import deque
import sys

cmd_line = int(input())
my_deque = deque()

for _ in range(cmd_line):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push_back":
        my_deque.append(cmd[1])
    elif cmd[0] == "push_front":
        my_deque.appendleft(cmd[1])
    elif cmd[0] == "front":
        if not my_deque:
            print("-1")
        else:
            print(my_deque[0])
    elif cmd[0] == "back":
        if not my_deque:
            print("-1")
        else:
            print(my_deque[-1])
    elif cmd[0] == "size":
        print(len(my_deque))
    elif "pop" in cmd[0]:
        if not my_deque:
            print("-1")
        else:
            if cmd[0] == "pop_front":
                print(my_deque.popleft())
            elif cmd[0] == "pop_back":
                print(my_deque.pop())
    elif cmd[0] == "empty":
        if not my_deque:
            print("1")
        else:
            print("0")
