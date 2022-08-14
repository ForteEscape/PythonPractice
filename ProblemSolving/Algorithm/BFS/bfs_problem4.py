from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
move_locations = [-1, 1, 2]
board = [0 for _ in range(200002)]
visited = [0 for _ in range(200002)]
queue = deque()

visited[N] = 1
queue.append(N)
seconds = 0

while queue:
    current_pos = queue.popleft()

    if current_pos == K:
        print(board[current_pos])
        break

    for move in move_locations:
        if move == 2:
            next_pos = current_pos * move
        else:
            next_pos = current_pos + move

        if 0 <= next_pos < 200002 and not visited[next_pos]:
            board[next_pos] = board[current_pos] + 1
            visited[next_pos] = 1
            queue.append(next_pos)

