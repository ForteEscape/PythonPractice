
N = int(input())
ans = 0

for _ in range(N):
    data = input()
    character = []
    is_group = True

    for i in range(len(data)):
        if data[i] not in character:
            character.append(data[i])
        else:
            if data[i - 1] != data[i]:
                is_group = False
                break

    if not is_group:
        continue
    else:
        ans += 1

print(ans)
