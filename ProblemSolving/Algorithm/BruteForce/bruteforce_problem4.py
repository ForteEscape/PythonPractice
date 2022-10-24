# 마인크래프트 no.18111
import sys

N, M, B = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
time_min = 1e9
mx = -1e9
time = 0


def get_need_block():
    max_value = []
    for element in board:
        max_value.append(max(element))
    mx_value = max(max_value)

    block = 0
    for i in range(N):
        for j in range(M):
            block += mx_value - board[i][j]

    return block, mx_value

# 시간 최소 구하기
# 1. 현재 맵 상태에서 놓을 블록 수가 충분할 경우에 균등하게 놓는 시간
# 2. 현재 맵 상태에서 최대 값 높이를 가진 공간을 깍고, 나머지 공간에 대해 균등하게 놓는 시간
# 1번이 최소가 될 경우 블록을 놓기만 해도 끝나기 때문에 1번이 최소 시간을 만족한다.
# 2번이 최소가 될 경우 아직 최소 값이 확정되지 않았으므로 시간 비교에서 1번이 최소가 될 때 까지 수행
# 2번에서 깍고 난 후 균등하게 된 것이 판정될 경우에 깍는데 걸린 시간과 1번 시간을 비교한다. 아닐 시엔 균등하게 만드는
# 시간을 측정하여 1번과 비교


while True:
    # 전체 맵이 균등하게 이루어졌는지를 확인
    need_block, mx = get_need_block()
    if need_block == 0:
        time_min = time
        break

    # 놓을 블럭의 수가 가지고 있는 블럭 수 보다 많을 경우 땅을 파는 것 이외엔 방법이 없음
    if need_block > B:
        for i in range(N):
            for j in range(M):
                if board[i][j] == mx:
                    time += 2
                    board[i][j] -= 1
                    B += 1
    else:
        comparator1, comparator2 = time, time

        need_block_c1, mx_c1 = get_need_block()
        comparator1 += need_block

        for i in range(N):
            for j in range(M):
                if board[i][j] == mx:
                    comparator2 += 2
                    board[i][j] -= 1
                    B += 1

        need_block_c2, mx_c2 = get_need_block()
        if need_block_c2 == 0:
            if comparator1 <= comparator2:
                time_min = comparator1
                mx = mx_c1
            else:
                time_min = comparator2
                mx = mx_c2
            break
        else:
            comparator2 += need_block_c2

            if comparator1 <= comparator2:
                time_min = comparator1
                mx = mx_c1
                break
            else:
                time = comparator2 - need_block_c2

print(time_min, mx)
