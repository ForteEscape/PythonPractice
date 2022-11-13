from collections import deque

N, M, S = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    E_a, E_b = map(int, input().split())
    graph[E_a].append(E_b)
    graph[E_b].append(E_a)

for element in graph:
    element.sort(reverse=True)

queue = deque([S])
visited[S] = 1
cnt = 2

while queue:
    cur = queue.popleft()

    for nx in graph[cur]:
        if not visited[nx]:
            visited[nx] = cnt
            cnt += 1
            queue.append(nx)

for i in range(1, N + 1):
    print(visited[i])


