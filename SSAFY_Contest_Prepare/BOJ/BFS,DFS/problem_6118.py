from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    E_a, E_b = map(int, input().split())
    graph[E_a].append(E_b)
    graph[E_b].append(E_a)

visited = [0 for _ in range(N + 1)]
queue = deque()
queue.append([1, 1])
visited[1] = 1
count = 2

while queue:
    cur, dist = queue.popleft()

    for nx in graph[cur]:
        if not visited[nx]:
            visited[nx] = dist + 1
            queue.append([nx, dist + 1])

cnt = 1
ans = 1
V = 1
for i in range(1, N + 1):
    if ans < visited[i]:
        cnt = 1
        ans = visited[i]
        V = i
    elif ans == visited[i]:
        cnt += 1

print(V, ans - 1, cnt)