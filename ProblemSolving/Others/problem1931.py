import sys

room = int(sys.stdin.readline().rstrip())

time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(room)]
time.sort(key= lambda x: (x[1], x[0]))

cnt = 0
end = 0

for s, e in time:
    if s >= end:
        cnt += 1
        end = e

print(cnt)
