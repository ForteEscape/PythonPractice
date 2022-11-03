from itertools import permutations

N = int(input())
data = [i for i in range(1, N + 1)]

per = permutations(data)

for element in per:
    print(*element)