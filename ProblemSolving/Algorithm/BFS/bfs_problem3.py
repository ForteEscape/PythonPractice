from collections import deque
import sys

width, height = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
queue = deque()
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
day = 0
final_x = 0
final_y = 0
tomato_cnt = width * height
tomato_bfs = 0

for y in range(height):
    for x in range(width):
        if board[y][x] == 1:
            queue.append([y, x])
            tomato_bfs += 1

        if board[y][x] == -1:
            tomato_cnt -= 1

while queue:
    current_y, current_x = queue.popleft()
    final_y, final_x = current_y, current_x

    for direction in directions:
        next_y = current_y + direction[0]
        next_x = current_x + direction[1]

        if 0 <= next_y < height and 0 <= next_x < width and not board[next_y][next_x]:
            board[next_y][next_x] = board[current_y][current_x] + 1
            queue.append([next_y, next_x])
            tomato_bfs += 1

if tomato_cnt != tomato_bfs:
    print("-1")
else:
    print(board[final_y][final_x] - 1)