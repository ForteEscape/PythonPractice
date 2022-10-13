import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
ans = [0 for _ in range(N + 1)]


def bfs():
    visited = [False for _ in range(N + 1)]
    visited[1] = True
    queue = deque()
    queue.append(1)

    while queue:
        current_node = queue.popleft()

        for next_node in graph[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                ans[next_node] = current_node
                queue.append(next_node)


for i in range(N - 1):
    node, linked_node = map(int, sys.stdin.readline().split())
    graph[node].append(linked_node)
    graph[linked_node].append(node)

bfs()

for i in range(2, N + 1):
    print(ans[i])