# BOJ 13335 answer code
from collections import deque
import sys

truck_num, bridge_len, bridge_weight = map(int, sys.stdin.readline().split())
truck_weight = list(map(int, sys.stdin.readline().split()))

ans = 0
current_weight = 0
bridge_queue = deque()
truck_queue = deque(truck_weight)

while True:
    ans += 1

    if bridge_queue and bridge_queue[0][1] > bridge_len:
        current_weight -= bridge_queue.popleft()[0]

    if truck_queue and current_weight + truck_queue[0] <= bridge_weight and len(bridge_queue) <= bridge_len:
        bridge_queue.append([truck_queue.popleft(), 1])
        current_weight += bridge_queue[-1][0]

    if not bridge_queue and not truck_queue:
        break

    for truck_in_bridge in bridge_queue:
        truck_in_bridge[1] += 1

print(ans)


