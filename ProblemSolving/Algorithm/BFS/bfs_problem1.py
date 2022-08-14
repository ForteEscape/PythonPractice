# BOJ 1926 answer code
from collections import deque
import sys

height, width = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
queue = deque()
pic_count = 0
area = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for y in range(height):
    for x in range(width):
        tmp_area = 0

        if board[y][x] == 1:
            pic_count += 1
            queue.append([y, x])
            board[y][x] = -1

            while queue:
                tmp_area += 1
                current_y, current_x = queue.popleft()

                for index in directions:
                    next_y = current_y + index[0]
                    next_x = current_x + index[1]

                    if 0 <= next_x < width and 0 <= next_y < height and board[next_y][next_x] == 1:
                        board[next_y][next_x] = -1
                        queue.append([next_y, next_x])

        if tmp_area > area:
            area = tmp_area


print(pic_count)
print(area)
