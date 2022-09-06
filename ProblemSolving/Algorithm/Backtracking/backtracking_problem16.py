# 소문난 칠공주
import sys
from collections import deque

board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]
group_location = [-1 for _ in range(7)]  # 각 공주들의 위치
ans = 0


def solve(cur_length, y_cnt, idx):
    if y_cnt > 3:
        return

    if cur_length == 7:
        if chk():
            global ans
            ans += 1
        return

    if idx == 25:
        return

    row = idx // 5
    col = idx % 5
    group_location[cur_length] = (row, col)

    solve(cur_length + 1, y_cnt + 1 if board[row][col] == 'Y' else y_cnt, idx + 1)
    solve(cur_length, y_cnt, idx + 1)
    return


def chk():
    visited = [[False for _ in range(5)] for _ in range(5)]
    cnt = 1

    for i in range(1, 7):
        visited[group_location[i][0]][group_location[i][1]] = True

    queue = deque()
    queue.append([group_location[0][0], group_location[0][1]])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        cur_y, cur_x = queue.popleft()

        for direction in directions:
            ny = cur_y + direction[0]
            nx = cur_x + direction[1]

            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx]:
                visited[ny][nx] = False
                cnt += 1
                queue.append([ny, nx])
                if cnt == 7:
                    return True

    return False


solve(0, 0, 0)
print(ans)