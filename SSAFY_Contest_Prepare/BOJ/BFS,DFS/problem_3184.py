from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
result_wolf, result_sheep = 0, 0

for i in range(N):
    for j in range(M):
        wolf_cnt, sheep_cnt = 0, 0
        wolf_location, sheep_location = [], []

        if (board[i][j] == '.' or board[i][j] == 'o' or board[i][j] == 'v') and not visited[i][j]:
            visited[i][j] = True
            queue.append([i, j])

        while queue:
            y, x = queue.popleft()

            if board[y][x] == 'o':
                sheep_cnt += 1
                sheep_location.append([y, x])
            elif board[y][x] == 'v':
                wolf_cnt += 1
                wolf_location.append([y, x])

            for direction in directions:
                ny = y + direction[0]
                nx = x + direction[1]

                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue

                if board[ny][nx] != '#' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx])

        if sheep_cnt > wolf_cnt:
            wolf_cnt = 0
            for location in wolf_location:
                board[location[0]][location[1]] = '.'
        else:
            sheep_cnt = 0
            for location in sheep_location:
                board[location[0]][location[1]] = '.'

        result_wolf += wolf_cnt
        result_sheep += sheep_cnt

print(result_sheep, result_wolf)
