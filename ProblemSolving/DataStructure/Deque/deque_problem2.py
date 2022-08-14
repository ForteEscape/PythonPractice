# BOJ 5430 answer code
from collections import deque
import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    cmd = sys.stdin.readline().rstrip()
    array_size = int(sys.stdin.readline())
    array_input = sys.stdin.readline().rstrip()
    error_flag = False
    directions = 0

    array_input = array_input.strip("[")
    array_input = array_input.strip("]")

    deque_list = array_input.split(",")

    if array_size == 0:
        my_deque = deque()
    else:
        my_deque = deque(deque_list)

    for parse in cmd:
        if parse == "R":
            if directions == 0:
                directions = 1
            else:
                directions = 0
        elif parse == "D":
            if not my_deque:
                error_flag = True
                break
            else:
                if directions == 1:
                    my_deque.pop()
                else:
                    my_deque.popleft()

    temp_list = []
    while my_deque:
        if directions == 1:
            temp_list.append(my_deque.pop())
        else:
            temp_list.append(my_deque.popleft())

    if error_flag:
        print("error")
    else:
        print("[" + ','.join(list(map(str, temp_list))) + "]")
