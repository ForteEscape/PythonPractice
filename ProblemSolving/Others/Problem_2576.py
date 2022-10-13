datalist = []
for i in range(7):
    data = int(input())

    if data % 2 != 0:
        datalist.append(data)

if not datalist:
    print("-1")
else:
    print(sum(datalist))
    print(min(datalist))