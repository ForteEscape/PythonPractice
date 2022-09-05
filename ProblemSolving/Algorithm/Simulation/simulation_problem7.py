import sys
from collections import deque

board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(12)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
chain_cnt = 0

while True:
    queue = deque()
    queue_destroy = deque()
    visited = [[False for _ in range(6)] for _ in range(12)]

    for i in range(12):
        for j in range(6):
            cnt = 0
            if board[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                queue.append([i, j])
                cnt += 1

                # 순회하면서 빈 공간이 아닌 부분을 만날 때 마다 BFS로 몇개가 이어져 있는지 탐색
                # 4개 이상일 시 파괴 가능하므로 파괴에 쓰는 queue_destroy에 추가
                while queue:
                    y, x = queue.popleft()

                    for direction in directions:
                        ny = y + direction[0]
                        nx = x + direction[1]

                        if ny < 0 or ny >= 12 or nx < 0 or nx >= 6:
                            continue
                        if not visited[ny][nx] and board[ny][nx] == board[y][x]:
                            visited[ny][nx] = True
                            cnt += 1
                            queue.append([ny, nx])

                if cnt >= 4:
                    queue_destroy.append([i, j])

    if not queue_destroy:
        break
    else:
        chain_cnt += 1

    # 파괴 구현
    while queue_destroy:
        y, x = queue_destroy.popleft()
        target = board[y][x]
        board[y][x] = '.'

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if ny < 0 or ny >= 12 or nx < 0 or nx >= 6:
                continue
            if board[ny][nx] != '.' and board[ny][nx] == target:
                queue_destroy.append([ny, nx])

    # 남은 잔해 낙하 구현
    for i in range(10, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                temp = board[i][j]
                board[i][j] = '.'

                idx = 0
                for k in range(i + 1, 12):
                    if board[k][j] != '.':
                        idx = k - 1
                        break
                    else:
                        idx = k
                board[idx][j] = temp


print(chain_cnt)
