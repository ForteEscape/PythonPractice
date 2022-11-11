# 12051 프리셀 통계 - 답안 참조함
T = int(input())

for test_case in range(1, T + 1):
    N, P_D, P_G = map(int, input().split())
    ans = ''

    # 오늘 승률이 0이 아닌데 전체 승률이 0인 경우
    if P_D != 0 and P_G == 0:
        ans = 'Broken'
    elif P_D != 100 and P_G == 100:  # 오늘 승률이 100이 아닌데 전체 승률이 100인 경우
        ans = 'Broken'
    else:
        for i in range(1, N + 1):
            if ((i * P_D) / 100) % 1 == 0:  # 진행한 판 수 중 승리한 판이 정수인 경우 가능함
                ans = 'Possible'
                break
        else:
            ans = 'Broken'

    print("#{} {}".format(test_case, ans))
