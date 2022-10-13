import sys

data = sys.stdin.readline().rstrip()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
HG_code = ['aespa', 'baekjoon', 'cau', 'debug', 'edge', 'firefox', 'golang', 'haegang',
           'iu', 'java', 'kotlin', 'lol', 'mips', 'null', 'os', 'python', 'query', 'roka',
           'solvedac', 'tod', 'unix', 'virus', 'whale', 'xcode', 'yahoo', 'zebra']

transformed_data = []
temp = data

while True:
    flag = False

    for i in range(26):
        if HG_code[i] in data:
            flag = True
            transformed_data.append([alphabet[i], temp.find(HG_code[i])])
            data = data.replace(HG_code[i], '', 1)

    if not flag:
        break

ans = ''
if data == '':
    transformed_data = sorted(transformed_data, key=lambda x: x[1])
    for i in range(len(transformed_data)):
        ans += transformed_data[i][0]
    print("It's HG!")
    print(ans)
else:
    print("ERROR!")


