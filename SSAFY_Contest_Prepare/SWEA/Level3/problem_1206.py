for test_case in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    ans = 0
    for i in range(2, N - 2):
        max_height = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        if height[i] > max_height:
            ans += height[i] - max_height

    print("#{} {}".format(test_case, ans))