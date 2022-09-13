import sys
import math
from collections import deque

N, movement_min, movement_max = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    continuable = False
    queue = deque()

    for i in range(N):
        for j in range(N):
            cnt = 0
            distribute_list = []
            population_sum = 0

            # 모든 배열을 순회하며 BFS로 국경을 열 것인지 결정한다.
            if not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                population_sum += board[i][j]
                queue.append([i, j])
                distribute_list.append([i, j])

            while queue:
                y, x = queue.popleft()

                for direction in directions:
                    ny = y + direction[0]
                    nx = x + direction[1]

                    if ny < 0 or ny >= N or nx < 0 or nx >= N:
                        continue

                    if not visited[ny][nx] and movement_min <= abs(board[y][x] - board[ny][nx]) <= movement_max:
                        continuable = True
                        visited[ny][nx] = True
                        population_sum += board[ny][nx]
                        queue.append([ny, nx])
                        distribute_list.append([ny, nx])
                        cnt += 1

            # 순회를 마친 후 연합을 구성하고 연합 인구를 계산한다 이후 각 좌표해 대하여 인구수를 적용한다.
            # 연합이 구성되지 않으면 인구 이동이 일어나지 않으므로 그대로 진행된다.
            if cnt != 0:
                distribute_population = int(math.floor(population_sum / cnt))

                for element in distribute_list:
                    board[element[0]][element[1]] = distribute_population

    if not continuable:
        break
    ans += 1

print(ans)
