from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline())) for _ in range(R)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited_fire = [[0 for _ in range(C)] for _ in range(R)]
visited_escape = [[0 for _ in range(C)] for _ in range(R)]

queue_fire = deque()
queue_escape = deque()
ans = 0

for y in range(R):
    for x in range(C):
        if board[y][x] == 'F':
            visited_fire[y][x] = 1
            queue_fire.append([y, x])
        if board[y][x] == 'J':
            visited_escape[y][x] = 1
            queue_escape.append([y, x])

# 불의 번짐
while queue_fire:
    fire_current_y, fire_current_x = queue_fire.popleft()

    for direction in directions:
        fire_next_y = fire_current_y + direction[0]
        fire_next_x = fire_current_x + direction[1]

        if 0 <= fire_next_y < R and 0 <= fire_next_x < C and board[fire_next_y][fire_next_x] != '#' and not visited_fire[fire_next_y][fire_next_x]:
            visited_fire[fire_next_y][fire_next_x] = visited_fire[fire_current_y][fire_current_x] + 1
            queue_fire.append([fire_next_y, fire_next_x])

is_escape = False
while queue_escape:
    current_y, current_x = queue_escape.popleft()

    for direction in directions:
        next_y = current_y + direction[0]
        next_x = current_x + direction[1]

        if 0 <= next_x < C and 0 <= next_y < R:
            if board[next_y][next_x] != '#' and not visited_escape[next_y][next_x]:
                if not visited_fire[next_y][next_x] or visited_fire[next_y][next_x] > visited_escape[current_y][current_x] + 1:
                    visited_escape[next_y][next_x] = visited_escape[current_y][current_x] + 1
                    queue_escape.append([next_y, next_x])
        else:
            print(visited_escape[current_y][current_x])
            is_escape = True
            break

    if is_escape:
        break

if not is_escape:
    print("IMPOSSIBLE")
