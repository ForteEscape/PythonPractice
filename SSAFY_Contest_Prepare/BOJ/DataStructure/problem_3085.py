N = int(input())
board = [list(input()) for _ in range(N)]
answer = 0


def chk(arr):
    n = len(arr)
    ans = 1

    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1

            ans = max(ans, cnt)

        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1

            ans = max(ans, cnt)

    return ans


for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            tmp = chk(board)

            answer = max(answer, tmp)

            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < N:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            tmp = chk(board)

            answer = max(answer, tmp)

            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(answer)

