for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for col in range(100):
        col_data = []
        for element in range(100):
            if board[element][col] != 0:
                col_data.append([element, col, board[element][col]])

        if len(col_data) == 1 or len(col_data) == 0:
            continue

        for i in range(len(col_data) - 1):
            if col_data[i][2] == 1:
                if col_data[i + 1][2] == 2:
                    ans += 1

    print("#{} {}".format(test_case, ans))