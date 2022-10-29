# 13547 팔씨름
T = int(input())

for test_case in range(1, T + 1):
    result = input()
    win_cnt = 0

    for element in result:
        if element == 'o':
            win_cnt += 1

    win_cnt += 15 - len(result)

    if win_cnt >= 8:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")