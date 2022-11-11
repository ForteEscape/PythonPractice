import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
plus_location = []
minus_location = []
max_location = 0

result = 0

for element in num_list:
    if element > 0:
        plus_location.append(element)
    else:
        minus_location.append(element)

    if abs(element) > abs(max_location):
        max_location = element

minus_location = sorted(minus_location)
plus_location = sorted(plus_location, reverse=True)

for i in range(0, len(plus_location), M):
    if plus_location[i] != max_location:
        result += plus_location[i] * 2

for i in range(0, len(minus_location), M):
    if minus_location[i] != max_location:
        result += abs(minus_location[i]) * 2

result += abs(max_location)
print(result)