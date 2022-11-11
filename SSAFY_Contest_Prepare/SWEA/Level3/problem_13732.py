# 13732 정사각형 판정
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    location = []
    size = [x ** 2 for x in range(1, 20)]
    is_square = True
    cnt = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                location.append([i, j])
                cnt += 1

    if cnt not in size:
        print(f"#{test_case} no")
        continue

    cnt2 = 0
    for y in range(location[0][0], location[-1][0] + 1):
        for x in range(location[0][1], location[-1][1] + 1):
            if board[y][x] == '.':
                is_square = False
                break
            else:
                cnt2 += 1
        if not is_square:
            break

    if cnt != cnt2:
        is_square = False

    if not is_square:
        print(f"#{test_case} no")
    else:
        print(f"#{test_case} yes")