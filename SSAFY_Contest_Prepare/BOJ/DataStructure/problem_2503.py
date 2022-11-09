# 순열 사용문제
from itertools import permutations

N = int(input())
per = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(N):
    data, strike, ball = map(int, input().split())
    data = list(str(data))
    idx = 0

    for i in range(len(per)):
        strike_cnt, ball_cnt = 0, 0
        i -= idx

        for j in range(3):
            data[j] = int(data[j])
            if data[j] in per[i]:
                if j == per[i].index(data[j]):
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        if strike_cnt != strike or ball_cnt != ball:
            per.remove(per[i])
            idx += 1

print(len(per))