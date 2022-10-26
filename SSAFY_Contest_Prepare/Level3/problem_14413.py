# 14413 격자판 칠하기
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    is_correct = True
    baseline = 0
    mark = ['#', '.']
    idx = 0

    for i in range(N):
        if i != 0:
            idx = baseline + 1
        for j in range(M):
            if j == 0:
                baseline = idx
            if board[i][j] == '?':
                idx += 1
            else:
                if board[i][j] != mark[idx % 2]:
                    is_correct = False
                    break
                else:
                    idx += 1

            if not is_correct:
                break
        if not is_correct:
            break

    if is_correct:
        print(f"#{test_case} possible")
        continue

    idx = 1
    is_correct = True
    for i in range(N):
        if i != 0:
            idx = baseline + 1
        for j in range(M):
            if j == 0:
                baseline = idx
            if board[i][j] == '?':
                idx += 1
            else:
                if board[i][j] != mark[idx % 2]:
                    is_correct = False
                    break
                else:
                    idx += 1

            if not is_correct:
                break
        if not is_correct:
            break

    if is_correct:
        print(f"#{test_case} possible")
        continue
    else:
        print(f"#{test_case} impossible")