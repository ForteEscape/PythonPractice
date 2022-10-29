# 15612 체스판 위의 룩 배치
T = int(input())

for test_case in range(1, T + 1):
    board = [list(map(str, input())) for _ in range(8)]
    rook_location = []
    is_correct = True
    cnt = 0

    for i in range(8):
        for j in range(8):
            if board[i][j] == 'O':
                cnt += 1
                rook_location.append([i, j])

    if cnt != 8:
        print("#{} no".format(test_case))
        continue

    for i in range(8):
        for j in range(i + 1, 8):
            if rook_location[i][0] == rook_location[j][0]:  # 동일한 행에 존재할 경우
                is_correct = False
                break
            elif rook_location[i][1] == rook_location[j][1]:  # 동일한 열에 존재할 경우
                is_correct = False
                break
        if not is_correct:
            print("#{} no".format(test_case))
            break
    else:
        print("#{} yes".format(test_case))