board = [list(map(int, input().split())) for _ in range(5)]
ans = [list(map(int, input().split())) for _ in range(5)]

location = []

t = 0
is_found = False
is_bingo = False

for i in range(5):
    for j in range(5):
        t += 1
        is_found = False
        for k in range(5):
            for l in range(5):
                if ans[i][j] == board[k][l]:
                    is_found = True
                    location.append([k, l])
                    break
            if is_found:
                break

        cnt = 0
        for element in location:
            # column
            tmp = 0
            for j in range(element[0], element[0] + 5):
                if j >= 5:
                    break
                if [j, element[1]] in location:

                    tmp += 1
                else:
                    tmp = 0
                    break

            if tmp == 5:
                cnt += 1
            else:
                tmp = 0
            if cnt >= 3:
                is_bingo = True
                break
            # row
            for j in range(element[1], element[1] + 5):
                if j >= 5:
                    break
                if [element[0], j] in location:

                    tmp += 1
                else:
                    tmp = 0
                    break

            if tmp == 5:
                cnt += 1
            else:
                tmp = 0

            if cnt >= 3:
                is_bingo = True
                break

            for j in range(5):
                if element[0] + j >= 5 or element[1] + j >= 5:
                    break
                if [element[0] + j, element[1] + j] in location:
                    tmp += 1
                else:
                    tmp = 0
                    break

            if tmp == 5:
                cnt += 1
            else:
                tmp = 0

            if cnt >= 3:
                is_bingo = True
                break

            for j in range(5):
                if element[0] + j >= 5 or element[1] - j < 0:
                    break

                if [element[0] + j, element[1] - j] in location:

                    tmp += 1
                else:
                    tmp = 0
                    break

            if tmp == 5:
                cnt += 1
            else:
                tmp = 0

            if cnt >= 3:
                is_bingo = True
                break
        if is_bingo:
            break
    if is_bingo:
        break

print(t)




