import sys

N = int(sys.stdin.readline().rstrip())

score = [100, 100]

for _ in range(N):
    m, n = map(int, sys.stdin.readline().split())

    if m > n:
        score[1] -= m
    elif m < n:
        score[0] -= n

print(score[0])
print(score[1])