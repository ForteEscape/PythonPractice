T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    board = []
    ans = []
    N, M = map(int, input().split())

    for i in range(N):
        temp = list(map(int, input().split()))
        board.append(temp)

    for i in range(N - M + 1):
        area = board[i:i + M]
        for j in range(N - M + 1):
            fly_area = []
            for element in area:
                if j == N - M:
                    temp = element[j:]
                else:
                    temp = element[j: j + M]
                fly_area.append(temp)
            print("fly_area: ", fly_area)
            s = 0
            for element in fly_area:
                s += sum(element)
            ans.append(s)
    print(f"#{test_case} {max(ans)}")