import heapq
import sys

N = int(sys.stdin.readline().rstrip())
cards = []
ans = 0

for i in range(N):
    cards.append(int(sys.stdin.readline().rstrip()))

heapq.heapify(cards)

while True:
    if len(cards) == 1:
        break
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    ans += a + b
    heapq.heappush(cards, a + b)

print(ans)
