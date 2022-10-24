import sys
N = int(sys.stdin.readline().rstrip())
road_length = list(map(int, sys.stdin.readline().split()))
city_weight = list(map(int, sys.stdin.readline().split()))
total_weight = 0

# 각 도시에 리터당 가격을 생각할 때, 자신보다 작은 가격을 가진 도시를 찾을 때 까지의 거리를 계산한다.
# 이후 가격에 리터 * 계산된 거리를 합치고, 이동한다.
idx = 0
length = len(city_weight)

while idx < length - 1: # 끝에 도달하면 끝나기 때문에
    road_weight = 0
    destination = 0

    for i in range(idx + 1, length):
        road_weight += road_length[i - 1]
        if city_weight[idx] > city_weight[i]:
            destination = i
            break
    else:
        destination = length - 1

    total_weight += city_weight[idx] * road_weight
    idx = destination

print(total_weight)
