from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while True:
    cnt = 0

    queue_ice = deque()
    queue_water = deque()
    visited_ice = [[0 for _ in range(M)] for _ in range(N)]
    visited_water = [[0 for _ in range(M)] for _ in range(N)]

    # 행 열의 각 첫줄은 무조건 0 이므로 빙하의 BFS에서 탐색 범위에 추가시키지 않는다.
    # 빙하의 조각 개수 탐색 BFS
    for y in range(1, N - 1):
        for x in range(1, M - 1):
            if board[y][x] != 0 and not visited_ice[y][x]:
                visited_ice[y][x] = 1
                queue_ice.append([y, x])
                cnt += 1

            while queue_ice:
                current_y, current_x = queue_ice.popleft()

                for direction in directions:
                    next_y = current_y + direction[0]
                    next_x = current_x + direction[1]

                    if 0 <= next_x < M and 0 <= next_y < N and board[next_y][next_x] and not visited_ice[next_y][next_x]:
                        visited_ice[next_y][next_x] = 1
                        queue_ice.append([next_y, next_x])

    if cnt >= 2:
        print(time)
        break

    if cnt == 0:
        print("0")
        break

    # 물에 의해 녹는 빙하를 BFS로 구현
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0 and not visited_water[y][x]:
                visited_water[y][x] = 1
                queue_water.append([y, x])

            while queue_water:
                current_y, current_x = queue_water.popleft()

                for direction in directions:
                    next_y = current_y + direction[0]
                    next_x = current_x + direction[1]

                    # 다음 좌표가 빙산인 경우
                    if 0 <= next_x < M and 0 <= next_y < N and board[next_y][next_x]:
                        visited_water[next_y][next_x] = 1
                        board[next_y][next_x] -= 1

                    # 다음 좌표가 물인 경우
                    if 0 <= next_x < M and 0 <= next_y < N and not board[next_y][next_x] and not visited_water[next_y][next_x]:
                        visited_water[next_y][next_x] = 1
                        queue_water.append([next_y, next_x])
    time += 1
