N = int(input())
play_count = list(map(int, input().split()))
play_count.sort(reverse=True)

# 탈 수 있는게 1개 말곤 없는 경우 무조건 그 하나만 타고 끝이다
if N == 1:
    print(1)
    exit(0)

sm = sum(play_count[1:])

# 가장 큰 이용횟수와 그 이전까지의 이용횟수의 합의 차이가 2 미만이라면 어떠한 경우에도 모두 탈 수 있다.
if play_count[0] - sm < 2:
    print(sm + play_count[0])
else:
    # 가장 큰 이용횟수와 그 이전까지의 이용횟수의 합의 차이가 2 이상이 날 시, 온전히 다 타지 못한다.
    # 온전히 다 타지 못하는 횟수는 위의 두 차이 - 1 만큼 된다.
    # 즉 sm + play_count[0] - (play_count[0] - sm - 1) 이 되고 이를 정리하면 (2 * sm) + 1이 된다.
    print((2 * sm) + 1)
