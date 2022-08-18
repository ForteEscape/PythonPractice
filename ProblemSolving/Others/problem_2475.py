import sys

data = list(map(int, sys.stdin.readline().split()))
code = 0

for element in data:
    code += (element ** 2)

print(code % 10)