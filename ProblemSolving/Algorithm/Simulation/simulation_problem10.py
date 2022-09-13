import sys

gear = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(4)]
rotate_cnt = int(sys.stdin.readline().rstrip())

for i in range(rotate_cnt):
    rotate_list = []
    g, d = map(int, sys.stdin.readline().split())

    rotate_list.append([g - 1, d])

    # 회전 여부 확인
    # 입력받은 톱니에서 1번 톱니까지 검사 만약 동일해서 돌지 않는다면 그 이후는 검사할 필요 없음
    pivot = rotate_list[0][0]
    direction = rotate_list[0][1]
    for idx in range(pivot, 0, -1):
        if gear[idx][6] != gear[idx - 1][2]:
            rotate_list.append([idx - 1, direction * -1])
            direction *= -1
        else:
            break

    # 입력받은 톱니에서 4번 톱니까지 검사 위와 동일함
    direction = rotate_list[0][1]
    for idx in range(pivot, 3):
        if gear[idx][2] != gear[idx + 1][6]:
            rotate_list.append([idx + 1, direction * -1])
            direction *= -1
        else:
            break

    # 회전
    for rotate in rotate_list:
        rotate_gear = rotate[0]
        rotate_direction = rotate[1]

        # 시계방향 회전
        if rotate_direction == 1:
            temp = gear[rotate_gear][-1]
            for j in range(7, 0, -1):
                gear[rotate_gear][j] = gear[rotate_gear][j - 1]
            gear[rotate_gear][0] = temp
        # 반시계방향 회전
        else:
            temp = gear[rotate_gear][0]
            for j in range(7):
                gear[rotate_gear][j] = gear[rotate_gear][j + 1]
            gear[rotate_gear][-1] = temp

ans = 0
if gear[0][0] == 1:
    ans += 1
if gear[1][0] == 1:
    ans += 2
if gear[2][0] == 1:
    ans += 4
if gear[3][0] == 1:
    ans += 8

print(ans)