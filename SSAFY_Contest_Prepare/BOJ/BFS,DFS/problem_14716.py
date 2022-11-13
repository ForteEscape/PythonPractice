from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
visited = [[False] * M for _ in range(N)]
queue = deque()

ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            ans += 1
            visited[i][j] = True
            queue.append([i, j])

        while queue:
            y, x = queue.popleft()

            for direction in directions:
                ny = y + direction[0]
                nx = x + direction[1]

                if ny < 0 or ny >= N or nx < 0 or nx >= M:
                    continue
                if board[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx])

print(ans)
