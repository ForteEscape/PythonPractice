import sys

N, M = map(int, sys.stdin.readline().split())
licked_loc = list(map(int, sys.stdin.readline().split()))
licked_loc = sorted(licked_loc)

sealing_status = [False for _ in range(1001)]
ans = 0

for location in licked_loc:
    if not sealing_status[location]:
        for i in range(location, location + M):
            if i > 1000:
                continue
            sealing_status[i] = True

        ans += 1

print(ans)
