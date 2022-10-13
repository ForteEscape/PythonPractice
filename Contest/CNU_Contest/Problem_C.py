import sys

length = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
odd_list = []
even_list = []
cnt = 1

for element in data:
    if element % 2 == 0:
        even_list.append(element)
    else:
        odd_list.append(element)

len_even = len(even_list)
len_odd = len(odd_list)

while True:
    if len_even == 0 and len_odd == 0:
        print("1")
        break

    if cnt % 2 != 0:
        if len_odd <= 0:
            if len_even != 0:
                print("0")
                break
            else:
                continue
        len_odd -= 1
    else:
        if len_even <= 0:
            if len_odd != 0:
                print("0")
                break
            else:
                continue
        len_even -= 1

    cnt += 1

