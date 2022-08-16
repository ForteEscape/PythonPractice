from collections import deque
import sys

while True:
    L, R, C = map(int, sys.stdin.readline().split())

    if L == 0 and R == 0 and C == 0:
        break

    building = []
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    queue = deque()

    is_escape = False
    directions = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, -1, 0], [0, 0, -1], [-1, 0, 0]]

    for floor in range(L):
        building.append(list(list(map(str, sys.stdin.readline().rstrip())) for _ in range(R + 1)))

    for h in range(L):
        for y in range(R):
            for x in range(C):
                if building[h][y][x] == 'S':
                    visited[h][y][x] = 1
                    queue.append([h, y, x])

                while queue:
                    current_h, current_y, current_x = queue.popleft()

                    if building[current_h][current_y][current_x] == 'E':
                        print("Escaped in", visited[current_h][current_y][current_x] - 1, "minute(s).")
                        is_escape = True
                        break

                    for direction in directions:
                        next_h = current_h + direction[0]
                        next_y = current_y + direction[1]
                        next_x = current_x + direction[2]

                        if 0 <= next_h < L and 0 <= next_y < R and 0 <= next_x < C:
                            if building[next_h][next_y][next_x] != '#' and not visited[next_h][next_y][next_x]:
                                visited[next_h][next_y][next_x] = visited[current_h][current_y][current_x] + 1
                                queue.append([next_h, next_y, next_x])
                if is_escape:
                    break
            if is_escape:
                break
        if is_escape:
            break
    if not is_escape:
        print("Trapped!")
