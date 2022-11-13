from collections import deque

N, M, S = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for element in graph:
    element.sort()

queue = deque([S])
visited[S] = 1
count = 2
while queue:
    cur = queue.popleft()

    for nx in graph[cur]:
        if not visited[nx]:
            visited[nx] = count
            count += 1
            queue.append(nx)

for i in range(1, N + 1):
    print(visited[i])