# 센서
import sys

N = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
sensor = list(map(int, sys.stdin.readline().split()))

if K >= N:
    print(0)
else:
    dist = []

    sensor = sorted(sensor)

    for i in range(1, N):
        dist.append(sensor[i] - sensor[i - 1])

    dist = sorted(dist)

    for _ in range(K - 1):
        dist.pop()

    print(sum(dist))
