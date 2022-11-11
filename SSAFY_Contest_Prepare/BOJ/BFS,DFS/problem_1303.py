from collections import deque

M, N = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
blue_power, white_power = 0, 0

for i in range(N):
    for j in range(M):
        cnt = 0
        kind = ''
        if not visited[i][j]:
            kind = board[i][j]
            visited[i][j] = True
            queue.append([i, j])

        while queue:
            y, x = queue.popleft()
            cnt += 1

            for direction in directions:
                ny = y + direction[0]
                nx = x + direction[1]

                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if not visited[ny][nx] and board[ny][nx] == kind:
                    visited[ny][nx] = True
                    queue.append([ny, nx])

        if kind == 'W':
            white_power += (cnt * cnt)
        elif kind == 'B':
            blue_power += (cnt * cnt)

print(white_power, blue_power)

