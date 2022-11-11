N = int(input())

# table[i] = 높이 i인 피자 기둥을 모두 i개의 높이 1인 기둥이 될 때 까지 나누었을 때 얻을 수 있는 즐거움의 최대값
table = [0] * ((10 ** 9) + 1)

# 높이 1인 기둥은 더 이상 나누지 않으므로 즐거음은 0이 된다. 높이 2인 기둥은 1, 1로 나누어지므로 즐거움은 1이 된다.
table[1] = 0
table[2] = 1

for i in range(3, N + 1):
    if i % 2 == 0:
        table[i] = (i // 2) ** 2 + table[i // 2] + table[i // 2]
    else:
        table[i] = (i // 2) * ((i // 2) + 1) + table[i // 2] + table[(i // 2) + 1]

print(table[N])