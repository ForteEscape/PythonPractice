from collections import deque
import sys

tc = int(sys.stdin.readline().rstrip())

while tc:
    tc -= 1

    N, M = map(int, sys.stdin.readline().split())
    doc_list = list(map(int, sys.stdin.readline().split()))
    ans = 0
    queue = deque()

    for element in enumerate(doc_list):
        queue.append(list(element))

    while queue:
        change_flag = False
        data = queue[0][1]

        for element in queue:
            if data < element[1]:
                change_flag = True
                break

        if change_flag:
            queue.append(queue.popleft())
        else:
            data = queue.popleft()
            ans += 1
            if data[0] == M:
                print(ans)
                break
