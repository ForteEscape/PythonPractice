import sys

N, K = map(int, sys.stdin.readline().split())
belt = list(map(int, sys.stdin.readline().split()))
robot = [False for _ in range(N)]
ans = 0

while True:
    ans += 1
    cnt = 0

    # 벨트가 로봇과 함께 이동
    temp = belt[-1]
    for i in range(N*2 - 1, 0, -1):
        belt[i] = belt[i - 1]
    belt[0] = temp

    temp = robot[-1]
    for i in range(N - 1, 0, -1):
        robot[i] = robot[i - 1]
    robot[0] = temp

    # 이동 후 로봇이 내리는 장소에 도착시 바로 내린다.
    if robot[N - 1]:
        robot[N - 1] = False

    # 가장 먼저 올라간 로봇은 가장 N에 가까운 위치에 있을 것이다.
    # 따라서 위치 N - 1에서 역순으로 돌며 만나는 모든 로봇을 순차적으로 방문후 검증
    for i in range(N - 2, 0, -1):
        if robot[i]:
            if not robot[i + 1] and belt[i + 1] != 0:
                robot[i], robot[i + 1] = robot[i + 1], robot[i]
                belt[i + 1] -= 1

    # 이동 후 로봇이 내리는 장소에 도착시 바로 내린다.
    if robot[N - 1]:
        robot[N - 1] = False

    # 올리는 위치에 로봇 올리기
    if belt[0] != 0:
        robot[0] = True
        belt[0] -= 1

    for i in range(2*N):
        if belt[i] == 0:
            cnt += 1

    if cnt >= K:
        break

print(ans)
