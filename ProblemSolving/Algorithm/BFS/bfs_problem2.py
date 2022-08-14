from collections import deque
import sys

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(height)]

queue = deque()
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue.append([0, 0])

while queue:
    y, x = queue.popleft()

    for direction in directions:
        next_y = y + direction[0]
        next_x = x + direction[1]

        if 0 <= next_y < height and 0 <= next_x < width and board[next_y][next_x] == 1:
            board[next_y][next_x] = board[y][x] + 1
            queue.append([next_y, next_x])

print(board[height - 1][width - 1])

