import sys

N = int(sys.stdin.readline().rstrip())
weight = []

for i in range(N):
    weight.append(int(sys.stdin.readline().rstrip()))

weight.sort(reverse=True)

cnt = 1
temp = 0
rope_weight = 0
for i in range(N):
    temp = weight[i] * cnt
    if temp > rope_weight:
        rope_weight = temp
    cnt += 1

print(rope_weight)


