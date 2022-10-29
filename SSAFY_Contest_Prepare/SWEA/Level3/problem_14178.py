# 14178 1차원 정원
T = int(input())

for test_case in range(1, T + 1):
    N, d = map(int, input().split())
    cnt = 0
    tmp = 0

    for i in range(1 + d, N + 1, 2 * d + 1):
        tmp = i
        cnt += 1

    if 1 + d > N:
        cnt += 1

    if tmp + d + 1 <= N:
        cnt += 1

    print(f"#{test_case} {cnt}")
