from collections import deque

N = int(input())
maze = list(map(int, input().split()))
queue = deque()
queue.append([0, 0])
visited = [0 for _ in range(N)]

if N == 1:
    print(0)
    exit(0)

while queue:
    cur, dist = queue.popleft()

    for nx in range(cur + 1, cur + maze[cur] + 1):
        if nx >= N:
            continue

        if not visited[nx]:
            visited[nx] = dist + 1
            queue.append([nx, dist + 1])

print(visited[N - 1] if visited[N - 1] != 0 else -1)
