import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))

numbers = sorted(list(set(numbers)))
print(*numbers)