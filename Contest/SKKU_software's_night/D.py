import sys

sheep = 0
wolf = 0
N = int(input())
cnt = N // 2
ans = 0
asked_cnt = []

while len(asked_cnt) != 20:
    if asked_cnt:
        cnt = asked_cnt[-1] + (sheep - wolf)

    print("? {}".format(cnt))
    sys.stdout.flush()

    sheep_result = int(input())
    wolf = cnt - sheep_result
    sheep = sheep_result

    asked_cnt.append(cnt)

    if sheep == wolf:
        ans = cnt
        break

if ans == 0:
    print("! 0")
    sys.stdout.flush()
else:
    print("! {}".format(ans))
    sys.stdout.flush()
