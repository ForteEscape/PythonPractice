from itertools import combinations
T = int(input())

for test_case in range(1, T + 1):
    ans = 0
    N, K = map(int, input().split())
    data = list(map(int, input().split()))

    for i in range(1, N + 1):
        per = list(combinations(data, i))

        for element in per:
            result = sum(element)

            if result == K:
                ans += 1

    print("#{} {}".format(test_case, ans))
