import copy

N = int(input())
current_status = list(input())
result_status = list(input())

current_status = list(map(int, current_status))
result_status = list(map(int, result_status))
mn_cnt = 1e9

for i in range(2):
    cnt = 0
    data = copy.deepcopy(current_status)

    # 0번 버튼을 누른 경우
    if i == 0:
        data[0] = 1 - data[0]

        if N > 1:
            data[1] = 1 - data[1]
        cnt += 1

    for j in range(1, N):
        if data[j - 1] != result_status[j - 1]:
            cnt += 1
            data[j - 1] = 1 - data[j - 1]
            data[j] = 1 - data[j]

            # j + 1 에 대한 OOB 검증
            if j + 1 < N:
                data[j + 1] = 1 - data[j + 1]

    for j in range(N):
        if data[j] != result_status[j]:
            break
    else:
        mn_cnt = min(mn_cnt, cnt)

if mn_cnt == 1e9:
    print(-1)
else:
    print(mn_cnt)