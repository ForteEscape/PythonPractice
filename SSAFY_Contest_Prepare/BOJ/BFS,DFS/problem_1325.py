from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


def bfs(start):
    cnt = 1
    queue = deque([start])
    visited = [False for _ in range(N + 1)]
    visited[start] = True

    while queue:
        cur = queue.popleft()

        for nx in graph[cur]:
            if not visited[nx]:
                visited[nx] = True
                cnt += 1
                queue.append(nx)

    return cnt


for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

mx_cnt = 1
ans = []
for i in range(1, N + 1):
    cnt = bfs(i)

    if cnt > mx_cnt:
        mx_cnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == mx_cnt:
        ans.append(i)

print(*ans)