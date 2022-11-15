M, N = map(int, input().split())
store = int(input())


def distance(direction, dist):
    if direction == 1:
        return dist
    if direction == 2:
        return M + N + M - dist
    if direction == 3:
        return 2 * M + N + N - dist
    if direction == 4:
        return M + dist


data = []
for _ in range(store + 1):
    direction, dist = map(int, input().split())
    data.append(distance(direction, dist))

ans = 0

for i in range(store):
    clock_dir = abs(data[-1] - data[i])
    # 시계방향으로 돈 데이터에 역으로 한바퀴 돈 길이를 뺀다.
    rev_clock_dir = 2 * (M + N) - clock_dir
    ans += min(clock_dir, rev_clock_dir)

print(ans)
