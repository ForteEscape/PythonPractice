for test_case in range(1, 11):
    dump_cnt = int(input())
    height = list(map(int, input().split()))

    while dump_cnt > 0:
        max_height = max(height)
        min_height = min(height)

        if max_height - min_height <= 1:
            break

        height[height.index(max_height)] -= 1
        height[height.index(min_height)] += 1
        dump_cnt -= 1

    max_height = max(height)
    min_height = min(height)

    print("#{} {}".format(test_case, max_height - min_height))