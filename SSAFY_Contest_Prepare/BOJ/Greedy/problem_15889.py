N = int(input())
location = list(map(int, input().split()))
flag = False

if N == 1:
    print("권병장님, 중대장님이 찾으십니다")
    exit(0)

shoot_range = list(map(int, input().split()))
shoot_range.append(0)
dataset = []
for i in range(N):
    dataset.append((location[i], shoot_range[i]))

dataset = sorted(dataset, key=lambda x: (x[0], x[1]))
idx = 0

while True:
    # 해당 위치와 사거리의 합이 마지막 사람의 좌표보다 크거나 같다면 가능하단 것으로 탈출
    if dataset[idx][0] + dataset[idx][1] >= dataset[N - 1][0]:
        break

    # 그것이 아니라면 현재 위치와 그 사람의 사거리의 합보다 큰 위치가 나올때까지 찾는다.
    for i in range(idx + 1, N):
        if dataset[idx][0] + dataset[idx][1] < dataset[i][0]:
            idx = i - 1
            break

    # 위치와 사거리의 합이 바로 다음 번의 사람에게 넘길 수 없다면 도달 불가능이므로 break
    if dataset[idx][0] + dataset[idx][1] < dataset[idx + 1][0]:
        flag = True
        break

if flag:
    print("엄마 나 전역 늦어질 것 같아")
else:
    print("권병장님, 중대장님이 찾으십니다")