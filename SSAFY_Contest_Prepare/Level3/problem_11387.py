# 11387 몬스터 사냥
T = int(input())

for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    damage = int(D * N + D * N * (N - 1) * L * 0.01 * 0.5)

    print("#{} {}".format(test_case, damage))