from collections import deque
import sys

length = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(length)]

low = min(map(min, board))
high = max(map(max, board))
ans = 0
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 모든 높이가 동일한 경우 모두 잠기거나 잠기지 않거나 의 두 가지 경우
if low == high:
    print("1")
else:
    for flood in range(low - 1, high):
        queue = deque()
        tmp_ans = 0
        visited = [[0 for _ in range(length)] for _ in range(length)]
        for y in range(length):
            for x in range(length):
                if board[y][x] > flood and not visited[y][x]:
                    visited[y][x] = 1
                    tmp_ans += 1
                    queue.append([y, x])

                while queue:
                    current_y, current_x = queue.popleft()

                    for direction in directions:
                        next_y = current_y + direction[0]
                        next_x = current_x + direction[1]

                        if 0 <= next_y < length and 0 <= next_x < length and board[next_y][next_x] > flood and not visited[next_y][next_x]:
                            visited[next_y][next_x] = 1
                            queue.append([next_y, next_x])

        if tmp_ans >= ans:
            ans = tmp_ans
    print(ans)

