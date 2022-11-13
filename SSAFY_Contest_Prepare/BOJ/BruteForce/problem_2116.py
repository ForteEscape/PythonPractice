N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

bottom_up_data = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

bottom_side_data = {
    5: [1, 2, 3, 4],
    4: [0, 1, 3, 5],
    3: [0, 2, 4, 5],
    2: [0, 1, 3, 5],
    1: [0, 2, 4, 5],
    0: [1, 2, 3, 4]
}


max_total = 0

for i in range(6):
    top_data = bottom_up_data[i]
    top_num = data[0][top_data]
    side_data = bottom_side_data[i]

    side_nums = []
    for idx in side_data:
        num = data[0][idx]
        side_nums.append(num)

    max_num = max(side_nums)

    for j in range(1, len(data)):
        bottom_idx = data[j].index(top_num)
        top_idx = bottom_up_data[bottom_idx]
        top_num = data[j][top_idx]

        side_data = bottom_side_data[bottom_idx]

        side_nums = []
        for idx in side_data:
            num = data[j][idx]
            side_nums.append(num)

        max_num += max(side_nums)

    max_total = max(max_total, max_num)

print(max_total)
