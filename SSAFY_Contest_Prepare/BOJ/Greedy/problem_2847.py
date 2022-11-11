N = int(input())
score_list = []

for i in range(N):
    data = int(input())
    score_list.append(data)

if N == 1:
    print(0)
    exit(0)

cnt = 0

while True:
    is_correct = True
    for j in range(N - 1):
        if score_list[j] >= score_list[j + 1]:
            score_list[j] -= 1
            cnt += 1
            is_correct = False

    if is_correct:
        break

print(cnt)