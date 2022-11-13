N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            board[i][0] += board[i - 1][0]
        elif j == i:
            board[i][j] += board[i - 1][j - 1]
        else:
            board[i][j] += max(board[i - 1][j - 1], board[i - 1][j])

print(max(board[N - 1]))