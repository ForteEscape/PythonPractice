# 1859 백만장자 프로젝트
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    ans = 0
    pivot = price[-1]

    for i in range(N - 2, -1, -1):
        if pivot > price[i]:
            ans += pivot - price[i]
        else:
            pivot = price[i]

    print(f"#{test_case} {ans}")