from collections import deque
import sys

while True:
    width, height = map(int, sys.stdin.readline().split())

    if width == 0 and height == 0:
        break

    directions = [[1, 0], [1, 1], [-1, 1], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, -1]]
    land_cnt = 0
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    visited = [[0 for _ in range(51)] for _ in range(51)]
    queue = deque()

    for y in range(height):
        for x in range(width):
            if board[y][x] and not visited[y][x]:
                land_cnt += 1
                visited[y][x] = 1
                queue.append([y, x])

            while queue:
                current_y, current_x = queue.popleft()

                for direction in directions:
                    next_y = current_y + direction[0]
                    next_x = current_x + direction[1]

                    if 0 <= next_y < height and 0 <= next_x < width and board[next_y][next_x] and not visited[next_y][next_x]:
                        visited[next_y][next_x] = 1
                        queue.append([next_y, next_x])

    print(land_cnt)


