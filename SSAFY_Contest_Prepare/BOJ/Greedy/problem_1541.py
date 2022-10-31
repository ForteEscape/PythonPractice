# 풀이 아이디어
# - 이후에 나오는 식들은 다음 - 가 나오기 전까지 모두 더하는 것이 전체 식을 최소로 만든다.
# ex) 30 + 40 - 50 + 30 - 20 + 10 - 10 - 20 이라는 식이 있다면
# (30 + 40) - (50 + 30) - (20 + 10) - 10 - 20 이 최소가 될 것이다.
# 따라서 - 를 기준으로 식을 나누고, 나눈 식 안에서 모두 더하여 빼주면 된다.

data = input()

# - 를 기준으로 나눈다.
data = data.split("-")

dataset = []
# 각 요소에 + 기호가 있어 연산해야 한다면 이를 나누고, int로 형변환한다.
for element in data:
    tmp = element.split("+")
    tmp = list(map(int, tmp))
    dataset.append(tmp)

result = 0
for rows in range(len(dataset)):
    if rows == 0:
        # 식의 처음은 무조건 숫자라고 되어있다 즉, 무조건 양수이다. 따라서 초항으로 해당 식의 결과를 계산하여 넣는다.
        result = sum(dataset[rows])
        continue
    
    # 이후에는 각 식 내부의 항들을 더하여 모두 뺀다. - 기호로 나누어지므로 무조건 빼주면 된다.
    result = result - sum(dataset[rows])

print(result)
