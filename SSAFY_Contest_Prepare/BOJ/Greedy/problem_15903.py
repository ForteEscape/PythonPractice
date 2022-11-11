import heapq

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

heapq.heapify(numbers)

for i in range(M):
    x = heapq.heappop(numbers)
    y = heapq.heappop(numbers)

    result = x + y
    heapq.heappush(numbers, result)
    heapq.heappush(numbers, result)

print(sum(numbers))
