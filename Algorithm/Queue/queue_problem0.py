from collections import deque
import sys

tc = int(input())
queue = deque()

for x in range(tc):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "front":
        if not queue:
            print("-1")
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if not queue:
            print("-1")
        else:
            print(queue[-1])
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if not queue:
            print("1")
        else:
            print("0")
    elif cmd[0] == "pop":
        if not queue:
            print("-1")
        else:
            data = queue[0]
            queue.popleft()
            print(data)