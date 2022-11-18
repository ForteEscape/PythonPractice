for test_case in range(1, 11):
    p_length = int(input())
    board = [list(input()) for _ in range(8)]
    ans = 0

    for i in range(8):
        for j in range((8 - p_length) + 1):
            data = board[i][j:j + p_length]
            original = data[:]
            data.reverse()
            if original == data:
                ans += 1

    for i in range((8 - p_length) + 1):
        for j in range(8):
            data = []
            for k in range(i, i + p_length):
                data.append(board[k][j])

            original = data[:]
            data.reverse()

            if original == data:
                ans += 1

    print("#{} {}".format(test_case, ans))