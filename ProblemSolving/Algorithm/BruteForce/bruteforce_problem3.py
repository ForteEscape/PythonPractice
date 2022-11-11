import sys

N = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False for _ in range(N)]
ans = 1e9


def solve(player_length, idx):
    global ans
    if player_length == N // 2:
        score_start = 0
        score_link = 0

        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    score_start += board[i][j]
                elif not visited[i] and not visited[j]:
                    score_link += board[i][j]

        ans = min(ans, abs(score_start - score_link))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            solve(player_length + 1, i + 1)
            visited[i] = False


solve(0, 0)
print(ans)
