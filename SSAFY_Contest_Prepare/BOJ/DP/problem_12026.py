N = int(input())
word = list(input())

# table = word[i]까지 갈 때의 최소 이동 값
table = [float('inf')] * (N + 1)
table[0] = 0

for i in range(1, N):
    for j in range(i):
        # 기준 위치의 character가 이전에 있던 위치의 character와 연속될 경우(연속됨 => B -> O -> J -> B)
        if word[j] == 'B' and word[i] == 'O':
            # 기존 위치까지의 최적해와 이전 위치의 최적해 + 기존 위치까지의 이동 가중치를 더한 것 중 최소를 선택
            table[i] = min(table[i], table[j] + (i - j) ** 2)
        elif word[j] == 'O' and word[i] == 'J':
            table[i] = min(table[i], table[j] + (i - j) ** 2)
        elif word[j] == 'J' and word[i] == 'B':
            table[i] = min(table[i], table[j] + (i - j) ** 2)

if table[N - 1] != float('inf'):
    print(table[N - 1])
else:
    print(-1)
