import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]


def bfs(r_graph, start_node):
    relation_step = [0] * (N + 1)
    visited = [start_node]
    queue = deque()
    queue.append(start_node)

    while queue:
        k = queue.popleft()

        for i in r_graph[k]:
            if i not in visited:
                relation_step[i] = relation_step[k] + 1
                visited.append(i)
                queue.append(i)

    return sum(relation_step)


for i in range(M):
    node, link_node = map(int, sys.stdin.readline().split())
    graph[node].append(link_node)
    graph[link_node].append(node)

result = []
for i in range(1, N + 1):
    result.append(bfs(graph, i))

print(result.index(min(result)) + 1)