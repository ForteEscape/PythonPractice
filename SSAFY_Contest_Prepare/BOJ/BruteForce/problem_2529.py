from itertools import permutations

N = int(input())
data = list(map(str, input().split()))
numbers = [i for i in range(10)]

# 부등호가 N개인 것은 numbers에서 N + 1 개의 순열을 만드는 것과 같다.
per = permutations(numbers, N + 1)
ans = []

# 뽑은 순열들을 검증하여 검증된 것이라면 답안 리스트에 넣는다.
for element in per:
    for j in range(len(element) - 1):
        if data[j] == '<' and element[j] > element[j + 1]:
            break
        elif data[j] == '>' and element[j] < element[j + 1]:
            break
    else:
        ans_data = ''
        for character in element:
            ans_data += str(character)
        ans.append(ans_data)

# 순열의 특성상 처음부터 끝까지 사전식으로 증가하므로, ans의 처음이 가장 작은 수고, 마지막이 가장 큰 수다
print(ans[-1])
print(ans[0])