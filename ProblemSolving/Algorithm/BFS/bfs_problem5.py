from collections import deque
import sys

T = int(sys.stdin.readline().rstrip())
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while T:
    T -= 1
    width, height, point = map(int, sys.stdin.readline().split())
    queue = deque()
    bugs = 0

    board = [[0 for _ in range(width)] for _ in range(height)]
    for _ in range(point):
        x, y = map(int, sys.stdin.readline().split())
        board[y][x] = 1

    for y in range(height):
        for x in range(width):
            if board[y][x] == 1:
                bugs += 1
                board[y][x] = -1
                queue.append([y, x])

            while queue:
                current_y, current_x = queue.popleft()

                for direction in directions:
                    next_y = current_y + direction[0]
                    next_x = current_x + direction[1]

                    if 0 <= next_x < width and 0 <= next_y < height and board[next_y][next_x] == 1:
                        board[next_y][next_x] = -1
                        queue.append([next_y, next_x])

    print(bugs)

