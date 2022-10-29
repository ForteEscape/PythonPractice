# 10912 외로운 문자
T = int(input())

for test_case in range(1, T + 1):
    data = input()
    character_dict = {}
    ans = []

    for character in data:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            del (character_dict[character])

    if not character_dict:
        print("#{} Good".format(test_case))
        continue

    for key in character_dict:
        ans.append(key)

    ans = sorted(ans)
    ans_str = ''.join(ans)

    print("#{} {}".format(test_case, ans_str))