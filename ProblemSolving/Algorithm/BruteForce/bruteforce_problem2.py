import sys
import copy

N, M = map(int, sys.stdin.readline().split())
board = []
ans = []
bw = ['B', 'W']

for i in range(N):
    data = list(sys.stdin.readline().rstrip())
    board.append(data)

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        cnt = 0

        row_idx = 0
        col_idx = 1
        new_board = []
        for k in range(8):
            new_data = [bw[col_idx % 2]]
            col_idx += 1
            for l in range(7):
                new_data.append(bw[row_idx % 2])
                row_idx += 1
            new_board.append(new_data)

        area = board[i:i + 8]
        compare_data = []
        for element in area:
            compare_data.append(element[j: j + 8])

        for k in range(8):
            for l in range(8):
                if compare_data[k][l] != new_board[k][l]:
                    cnt += 1
        ans.append(cnt)

        cnt = 0

        row_idx = 1
        col_idx = 0

        new_board.clear()
        for k in range(8):
            new_data = [bw[col_idx % 2]]
            col_idx += 1
            for l in range(7):
                new_data.append(bw[row_idx % 2])
                row_idx += 1
            new_board.append(new_data)

        for k in range(8):
            for l in range(8):
                if compare_data[k][l] != new_board[k][l]:
                    cnt += 1
        ans.append(cnt)

print(min(ans))
