# 11315 오목 판정
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(str, input())) for _ in range(N)]
    is_five_mok = False
    cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                # 행
                for chk in range(j, j + 5):
                    if chk >= N:
                        break

                    if board[i][chk] != 'o':
                        cnt = 0
                        break
                    else:
                        cnt += 1
                if cnt >= 5:
                    is_five_mok = True
                    break
                else:
                    cnt = 0

                # 열
                for chk in range(i, i + 5):
                    if chk >= N:
                        break

                    if board[chk][j] != 'o':
                        cnt = 0
                        break
                    else:
                        cnt += 1
                if cnt >= 5:
                    is_five_mok = True
                    break
                else:
                    cnt = 0

                # 좌 - 우 대각선
                y, x = i, j
                for chk in range(5):
                    if y >= N or x >= N:
                        break

                    if board[y][x] != 'o':
                        cnt = 0
                        break
                    else:
                        cnt += 1

                    y += 1
                    x += 1
                if cnt >= 5:
                    is_five_mok = True
                    break
                else:
                    cnt = 0

                # 우 - 좌 대각선
                y, x = i, j
                for chk in range(5):
                    if y >= N or x < 0:
                        break

                    if board[y][x] != 'o':
                        cnt = 0
                        break
                    else:
                        cnt += 1

                    y += 1
                    x -= 1

                if cnt >= 5:
                    is_five_mok = True
                    break
                else:
                    cnt = 0
        if is_five_mok:
            break

    if is_five_mok:
        print("#{} YES".format(test_case))
    else:
        print("#{} NO".format(test_case))