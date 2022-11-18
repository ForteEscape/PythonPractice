from collections import deque
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = -1
    for i in range(1, V + 1):
        stack = deque([i])
        visited = [0 for _ in range(V + 1)]
        visited[i] = 1

        while stack:
            cur = stack.pop()

            for nv in graph[cur]:
                if not visited[nv]:
                    visited[nv] = visited[cur] + 1
                    stack.append(nv)

        ans = max(ans, )


    print("#{} {}".format(test_case, ans))