from collections import deque

N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
s_y, s_x = map(int, input().split())
guest_data = [list(map(int, input().split())) for _ in range(M)]
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
queue = deque()
visited = [[0 for _ in range(N)] for _ in range(N)]
visited[s_y - 1][s_x - 1] = 1

arrived_guest = []
queue.append([s_y - 1, s_x - 1])
is_cleared = True

while len(arrived_guest) != M:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[queue[0][0]][queue[0][1]] = 1
    guest = []
    distance_goal = 0

    # 최단거리에 위치한 승객을 찾는 BFS
    while queue:
        y, x = queue.popleft()

        # 승객이 해당 위치에 존재하는지 찾는다.
        for element in guest_data:
            # 이미 도착한 승객인지 확인한다.
            if element in arrived_guest:
                continue
            # 존재할 경우 탑승한다.
            if y == element[0] - 1 and x == element[1] - 1:
                distance_goal = visited[y][x]
                guest.append(element)

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not visited[ny][nx] and not board[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1

                if not guest:
                    queue.append([ny, nx])

    if not guest and len(arrived_guest) != M:
        is_cleared = False
        break

    guest.sort(key=lambda k: (k[0], k[1]))
    guest = guest[0]

    # 연료를 최단거리만큼 소모한다.
    fuel -= (distance_goal - 1)

    # 승객을 태울때 연료가 없다면 이송하지 못하므로 실패다.
    if fuel <= 0:
        is_cleared = False
        break

    # 출발지 재설정
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue.clear()
    queue.append([guest[0] - 1, guest[1] - 1])
    distance_goal = 0

    visited[guest[0] - 1][guest[1] - 1] = 1

    # 출발지 이동 BFS
    while queue:
        y, x = queue.popleft()

        if y == guest[2] - 1 and x == guest[3] - 1:
            distance_goal = visited[y][x]
            break

        for direction in directions:
            ny = y + direction[0]
            nx = x + direction[1]

            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not visited[ny][nx] and not board[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append([ny, nx])

    # 목적지까지 이동한 연료 양을 뺀다
    fuel -= (distance_goal - 1)
    # 이동한 시점에서 연료가 0보다 작다면 실패한 것으로 break한다.(도착순간 0은 도착으로 인정한다)
    if fuel < 0:
        is_cleared = False
        break

    fuel += (distance_goal - 1) * 2
    # 이동 좌표 다시 세팅
    queue.clear()
    queue.append([guest[2] - 1, guest[3] - 1])
    arrived_guest.append(guest)

if is_cleared:
    print(fuel)
else:
    print(-1)