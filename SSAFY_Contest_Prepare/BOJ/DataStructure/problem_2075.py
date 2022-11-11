import sys
import heapq

N = int(sys.stdin.readline().rstrip())
data = []

# 메모리 절약을 위해 1줄을 미리 heap에 저장한다.
for i in map(int, sys.stdin.readline().split()):
    heapq.heappush(data, i)

# 나머지 행을 입력받는다.
for i in range(1, N):
    tmp = list(map(int, sys.stdin.readline().split()))

    # min-heap 이므로 최소 값 보다 더 큰 데이터가 입력될 경우 최소값을 pop한다.
    # 이렇게 될 경우 min-heap 의 특성상 크기 5를 가지는 heap에서 가장 작은 값이 앞으로 온다.
    for j in range(N):
        if data[0] < tmp[j]:
            heapq.heappush(data, tmp[j])
            heapq.heappop(data)

print(data[0])