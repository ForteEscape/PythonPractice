import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
    data = list(map(int, sys.stdin.readline().split()))

    data_sorted = sorted(data)
    print(data_sorted[-3])
