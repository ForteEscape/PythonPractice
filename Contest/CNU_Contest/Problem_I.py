import math
import sys

limit = 1001
prime_array = [True for i in range(limit + 1)]

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

temp1 = [x for x in range(A, B + 1)]
temp2 = [x for x in range(C, D + 1)]

duplicate_area = []

for i in temp1:
    if i in temp2:
        duplicate_area.append(i)

for i in range(2, int(math.sqrt(limit)) + 1):
    if prime_array[i]:
        j = 2
        while i * j <= limit:
            prime_array[i * j] = False
            j += 1

cnt = 0
if duplicate_area:
    priority_start = min(duplicate_area)
    priority_end = max(duplicate_area)

while True:
    is_yt_failed = True
    is_yj_failed = True

    if duplicate_area:
        for i in range(priority_start, priority_end + 1):
            if cnt % 2 == 0:
                if prime_array[i]:
                    is_yt_failed = False
                    prime_array[i] = False
                    break
            else:
                if prime_array[i]:
                    is_yj_failed = False
                    prime_array[i] = False
                    break

        if cnt % 2 == 0 and is_yt_failed:
            for i in range(A, B + 1):
                if prime_array[i]:
                    is_yt_failed = False
                    prime_array[i] = False
                    break

        elif cnt % 2 != 0 and is_yj_failed:
            for i in range(C, D + 1):
                if prime_array[i]:
                    is_yj_failed = False
                    prime_array[i] = False
                    break
    else:
        if cnt % 2 == 0:
            for i in range(A, B + 1):
                if prime_array[i]:
                    is_yt_failed = False
                    prime_array[i] = False
                    break
        else:
            for i in range(C, D + 1):
                if prime_array[i]:
                    is_yj_failed = False
                    prime_array[i] = False
                    break

    if cnt % 2 == 0 and is_yt_failed:
        print("yj")
        break
    elif cnt % 2 != 0 and is_yj_failed:
        print("yt")
        break
    cnt += 1

