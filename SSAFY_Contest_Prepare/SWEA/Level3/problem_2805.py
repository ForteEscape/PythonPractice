T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    start = (N - 1) // 2
    ans = int(board[0][start])
    start, end = start - 1, start + 1

    # 0행 ~ (N - 1) // 2 행
    for i in range(1, (N - 1) // 2 + 1):
        for j in range(start, end + 1):
            ans += int(board[i][j])
        start = start - 1
        end = end + 1

    start = start + 2
    end = end - 2
    for i in range((N - 1) // 2 + 1, N):
        for j in range(start, end + 1):
            ans += int(board[i][j])
        start = start + 1
        end = end - 1

    print("#{} {}".format(test_case, ans))
