import sys

N = int(sys.stdin.readline().rstrip())
number_list = []
freq_dict = {}
result = 0

for i in range(N):
    k = int(sys.stdin.readline().rstrip())

    if k not in freq_dict:
        freq_dict[k] = 1
    else:
        freq_dict[k] += 1

    number_list.append(k)
    result += k

number_list.sort()

freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)
mx = freq[0][1]

flag = False
temp = [freq[0]]
for i in range(1, len(freq)):
    if freq[i][1] == mx:
        temp.append(freq[i])
        flag = True

print(round(result / N))
print(number_list[(N - 1) // 2])

if flag:
    temp = sorted(temp, key=lambda item: item[0])
    print(temp[1][0])
else:
    print(freq[0][0])

print(abs(max(number_list) - min(number_list)))
