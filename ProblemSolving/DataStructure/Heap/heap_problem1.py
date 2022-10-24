# 백준 최소 힙
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
my_heap = []

for i in range(N):
    operation = int(sys.stdin.readline().rstrip())

    if operation == 0:
        if not my_heap:
            print(0)
        else:
            print(heapq.heappop(my_heap))
    else:
        heapq.heappush(my_heap, operation)
