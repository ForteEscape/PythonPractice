import sys

R, C, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
cleaner_location = []

for i in range(R):
    if board[i][0] == -1:
        cleaner_location.append(i)

while T:
    T -= 1
    mask = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            cnt = 0

            # 맵을 순회하면서 먼지를 찾는다.
            if board[i][j] != -1 and board[i][j] != 0:
                weight = board[i][j] // 5

                # 확산의 구현 - 먼지의 좌표에서 상하좌우를 탐색하여 mask에 값을 저장
                for direction in directions:
                    y = i + direction[0]
                    x = j + direction[1]

                    if y < 0 or y >= R or x < 0 or x >= C or board[y][x] == -1:
                        continue

                    cnt += 1
                    mask[y][x] += weight

                # 확산이 끝날 시 본 좌표에 있는 먼지 에서 확산된 수 * 먼지 / 5만큼 감소
                mask[i][j] -= weight * cnt

    # 모든 확산 연산 종료시 board에 mask 계산값을 더하여 업데이트함
    for i in range(R):
        for j in range(C):
            board[i][j] += mask[i][j]

    # 바람에 의한 순환 구현 - 상단
    cleaner_upper_Y = cleaner_location[0]
    cleaner_upper_X = 0

    # 1열 상단에서 하단으로 하강
    for i in range(cleaner_upper_Y - 1, 0, -1):
        board[i][0] = board[i - 1][0]

    # 1행 우측에서 좌측으로 이동
    for j in range(0, C - 1):
        board[0][j] = board[0][j + 1]

    # C열 하단에서 상단으로 상승
    for i in range(0, cleaner_upper_Y):
        board[i][C - 1] = board[i + 1][C - 1]

    # cleaner_upper_Y행 좌측에서 우측으로 이동
    for j in range(C - 1, 1, -1):
        board[cleaner_upper_Y][j] = board[cleaner_upper_Y][j - 1]

    board[cleaner_upper_Y][1] = 0

    # 하단은 동일한 방식으로 역순으로 돌린다
    cleaner_low_Y = cleaner_location[1]
    cleaner_low_X = 0

    for i in range(cleaner_low_Y + 1, R - 1):
        board[i][0] = board[i + 1][0]

    for j in range(0, C - 1):
        board[R - 1][j] = board[R - 1][j + 1]

    for i in range(R - 1, cleaner_low_Y, -1):
        board[i][C - 1] = board[i - 1][C - 1]

    for j in range(C - 1, 1, -1):
        board[cleaner_low_Y][j] = board[cleaner_low_Y][j - 1]

    board[cleaner_low_Y][1] = 0

ans = 0
for i in range(R):
    for j in range(C):
        if board[i][j] != 0 and board[i][j] != -1:
            ans += board[i][j]

print(ans)