import sys

num = list(map(int, sys.stdin.readline().split()))

num = sorted(num)
print(*num)
