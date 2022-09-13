N = int(input())
num_list = []


def merge_sort(start, end):
    if end - start < 2:
        return

    mid = (start + end) // 2

    merge_sort(start, mid)
    merge_sort(mid, end)
    merge(start, end)


def merge(start, end):
    temp_list = []
    mid = (start + end) // 2
    left = start
    right = mid

    while left < mid and right < end:
        if num_list[left] < num_list[right]:
            temp_list.append(num_list[left])
            left += 1
        else:
            temp_list.append(num_list[right])
            right += 1

    while left < mid:
        temp_list.append(num_list[left])
        left += 1

    while right < end:
        temp_list.append(num_list[right])
        right += 1

    for i in range(start, end):
        num_list[i] = temp_list[i - start]


for i in range(N):
    num_list.append(int(input()))

merge_sort(0, len(num_list))

for i in range(N):
    print(num_list[i])
