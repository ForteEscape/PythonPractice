# 11856 반반
T = int(input())

for test_case in range(1, T + 1):
    L = list(input())
    data = list(set(L))
    res = []
    ans = ''

    if len(data) != 2:
        ans = 'No'
    else:
        for element in data:
            cnt = 0
            for j in L:
                if element == j:
                    cnt += 1
            if cnt != 2:
                ans = 'No'
                break
        else:
            ans = 'Yes'

    print("#{} {}".format(test_case, ans))