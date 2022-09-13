import sys

N, M = map(int, sys.stdin.readline().split())
card = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

candidate = []

for row in card:
    candidate.append(min(row))

print(max(candidate))