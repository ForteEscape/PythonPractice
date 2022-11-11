from collections import deque

remember_data = int(input())
line = list(input())

stack = deque()
diff = 0
cnt = 0
change_idx = -1

for i in range(len(line)):
    if not stack:
        stack.append(line[i])
        diff += 1
        cnt += 1
        continue

    if stack[-1] != line[i]:
        stack.pop()
        diff -= 1
        cnt += 1
    else:
        # stack top과 line[i] 가 같을 때 / 차이값이 한계에 달할 경우 처음과 두 번째의 갈아치우기가 가능
        # i + 1 이 OOB일 경우(i 가 list의 마지막일 때) 무조건 line[i]를 넣어야 하기 때문에 break
        # line[i]와 line[i + 1]이 같아 어느걸 넣어도 안될 경우 break
        if diff == remember_data:
            if i + 1 < len(line) and stack[-1] != line[i + 1]:
                # 교체하여 차이를 줄일 수 있는 경우, line[i], line[i + 1]을 swap
                line[i], line[i + 1] = line[i + 1], line[i]
                stack.pop()
                diff -= 1
                cnt += 1
            else:
                break
        # diff가 한계점에 달하지 않은 경우 그냥 push
        else:
            stack.append(line[i])
            diff += 1
            cnt += 1

print(cnt)

