import copy
import sys

N = int(sys.stdin.readline().rstrip())
str_list = []
alphabet_list = []
num_list = [x for x in range(9, -1, -1)]
str_dic = {}

for _ in range(N):
    data = sys.stdin.readline().rstrip()
    str_list.append(data)

    for i in range(len(data)):
        if data[i] not in str_dic:
            str_dic[data[i]] = 0

for element in str_list:
    for i in range(len(element)):
        num = 10 ** (len(element) - i - 1)
        str_dic[element[i]] += num

for value in str_dic.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)

sm = 0
for i in range(len(sorted_list)):
    sm += sorted_list[i] * (9 - i)

print(sm)



