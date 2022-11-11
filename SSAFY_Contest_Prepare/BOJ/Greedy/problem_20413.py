N = int(input())
grade_pivot = list(map(int, input().split()))
grade = list(input())
data = {'B': 0, 'S': 1, 'G': 2, 'P': 3}
spend_money = []

for element in grade:
    if element == 'D':
        spend_money.append(grade_pivot[3])
        continue

    if not spend_money:
        spend_money.append(grade_pivot[data[element]] - 1)
    else:
        spend_money.append(grade_pivot[data[element]] - 1 - spend_money[-1])

print(sum(spend_money))