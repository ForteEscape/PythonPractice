N = int(input())
rank_list = []

for i in range(N):
    predict_rank = int(input())
    rank_list.append(predict_rank)

rank_list.sort()
rank_pivot = 1

result = 0
for i in range(N):
    result += abs(rank_list[i] - rank_pivot)
    rank_pivot += 1

print(result)
