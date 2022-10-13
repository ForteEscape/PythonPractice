# 가장 작은 수를 가장 앞에 있는 수와 교대한다.
import sys

N = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
index = {}

sorted_num = sorted(numbers)

for i in range(N):
    index[numbers[i]] = i

cnt = 0
idx = 0

while idx < N - 1:
    mn_idx = index.get(sorted_num[idx])
    if mn_idx != idx:
        numbers[idx], numbers[mn_idx] = numbers[mn_idx], numbers[idx]
        index[numbers[mn_idx]], index[numbers[idx]] = index[numbers[idx]], index[numbers[mn_idx]]
        numbers[idx] = 1e9 + 1
        cnt += 1
        idx += 1
    else:
        numbers[idx] = 1e9 + 1
        idx += 1

print(cnt)
