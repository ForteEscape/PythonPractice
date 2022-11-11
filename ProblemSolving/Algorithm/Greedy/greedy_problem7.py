import sys

N = int(sys.stdin.readline().rstrip())
crane_weight = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())
box_weight = list(map(int, sys.stdin.readline().split()))

crane_weight = sorted(crane_weight, reverse=True)
box_weight = sorted(box_weight, reverse=True)

if crane_weight[0] < box_weight[0]:
    print(-1)
else:
    cnt = 0

    while box_weight:
        if not box_weight:
            break

        for crane in crane_weight:
            for box in box_weight:
                if crane >= box:
                    box_weight.remove(box)
                    break

        cnt += 1

    print(cnt)
