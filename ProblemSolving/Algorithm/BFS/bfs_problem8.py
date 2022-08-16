from collections import deque
import sys

F, S, G, U, D = map(int, sys.stdin.readline().split())
directions = [U, D*(-1)]
visited = [0 for _ in range(2000002)]

queue = deque()
queue.append(S)
visited[S] = 1
is_using_stairs = True

while queue:
    current_pos = queue.popleft()

    if current_pos == G:
        print(visited[G] - 1)
        is_using_stairs = False
        break

    for direction in directions:
        next_pos = current_pos + direction

        if 1 <= next_pos <= F and not visited[next_pos]:
            visited[next_pos] = visited[current_pos] + 1
            queue.append(next_pos)

if is_using_stairs:
    print("use the stairs")

