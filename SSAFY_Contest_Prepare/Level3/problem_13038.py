# 13038 교환학생
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = 1e9

    for i in range(7):
        start = 0
        cnt = 0
        cnt2 = 0
        if data[i] == 1:
            start = i

            while cnt2 != N:
                if data[start % 7] == 1:
                    cnt2 += 1
                cnt += 1
                start += 1

            ans = min(ans, cnt)

    print(f"#{test_case} {ans}")