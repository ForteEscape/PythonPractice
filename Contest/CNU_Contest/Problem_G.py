import sys

N, M = map(int, sys.stdin.readline().split())
str_list = []

if N == 1:
    print("1")
else:
    for i in range(N):
        str_list.append(sys.stdin.readline().rstrip())

    for i in range(1, N):
        prev_block = str_list[i - 1]
        current_block = str_list[i]

        is_stackable = False
        for idx in range(1, M + 1):
            block1 = prev_block[-idx:]
            block2 = current_block[:idx]

            if block1 == block2:
                is_stackable = True
                break

        if not is_stackable:
            print("0")
            break
    else:
        print("1")
