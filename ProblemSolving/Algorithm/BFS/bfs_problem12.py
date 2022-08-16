from collections import deque
import sys

C, R, H = map(int, sys.stdin.readline().split())
box = [list(list(map(int, sys.stdin.readline().split())) for _ in range(R)) for _ in range(H)]
directions = [[1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1], [-1, 0, 0]]
tomat_total = C * R * H
tomat_rotten = 0
ans = 0
queue = deque()

for h in range(H):
    for y in range(R):
        for x in range(C):
            if box[h][y][x] == -1:
                tomat_total -= 1
            elif box[h][y][x] == 1:
                queue.append([h, y, x])
                tomat_rotten += 1

f_h, f_y, f_x = 0, 0, 0

while queue:
    h, y, x = queue.popleft()
    f_h, f_y, f_x = h, y, x

    for direction in directions:
        nh = h + direction[0]
        ny = y + direction[1]
        nx = x + direction[2]

        if 0 <= nh < H and 0 <= ny < R and 0 <= nx < C and not box[nh][ny][nx]:
            box[nh][ny][nx] = box[h][y][x] + 1
            queue.append([nh, ny, nx])
            tomat_rotten += 1

if tomat_rotten != tomat_total:
    print("-1")
else:
    print(box[f_h][f_y][f_x] - 1)