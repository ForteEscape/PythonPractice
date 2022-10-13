import sys

N, M = map(int, sys.stdin.readline().split())

if N > M * 2:
    print(M)
else:
    print(N // 2)