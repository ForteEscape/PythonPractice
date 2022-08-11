from collections import deque

N, K = map(int, input().split())
queue_list = [x for x in range(1, N + 1)]
queue = deque(queue_list)
ans = []

while queue:
    queue.rotate(-(K - 1))
    ans.append(queue.popleft())

print("<" + ", ".join(list(map(str, ans))) + ">")


