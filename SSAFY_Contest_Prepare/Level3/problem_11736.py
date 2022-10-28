# 11736 평범한 숫자
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    queue = deque(data[:2])

    for i in range(1, N - 1):
        queue.append(data[i + 1])
        if data[i] != max(queue) and data[i] != min(queue):
            cnt += 1

        queue.popleft()

    print("#{} {}".format(test_case, cnt))