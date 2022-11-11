import sys
import heapq

N = int(sys.stdin.readline().rstrip())
timeline = []
heap = []

for i in range(N):
    S, T = map(int, sys.stdin.readline().split())
    timeline.append([S, T])

timeline = sorted(timeline, key=lambda x: x[0])
heapq.heappush(heap, timeline[0][1])

for i in range(1, N):
    if heap[0] > timeline[i][0]:
        heapq.heappush(heap, timeline[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, timeline[i][1])

print(len(heap))