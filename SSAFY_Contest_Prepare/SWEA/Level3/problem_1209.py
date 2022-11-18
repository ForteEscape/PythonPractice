for _ in range(10):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    mx_row = -1
    for element in board:
        mx_row = max(mx_row, sum(element))

    mx_col = -1
    for x in range(100):
        result = 0
        for y in range(100):
            result += board[y][x]
        mx_col = max(mx_col, result)

    cross_1 = 0
    for i in range(100):
        cross_1 += board[i][i]

    cross_2 = 0
    for i in range(99, -1, -1):
        cross_2 += board[i][i]

    ans = max(mx_row, mx_col, cross_1, cross_2)
    print("#{} {}".format(tc, ans))
