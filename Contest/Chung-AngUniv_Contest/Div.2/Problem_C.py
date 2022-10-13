import sys

N = int(sys.stdin.readline().rstrip())
table = [list(map(str, sys.stdin.readline().split())) for _ in range(N * 4)]
time_dict = {}
serv_time = [4, 6, 4, 10]
tot_time = []

for i in range(N * 4):
    for j in range(7):
        if table[i][j] == '-':
            continue

        if table[i][j] not in time_dict:
            time_dict[table[i][j]] = 0

        time_dict[table[i][j]] += serv_time[i % 4]

if not time_dict:
    print("Yes")
else:
    for key in time_dict:
        tot_time.append(time_dict[key])

    if max(tot_time) - min(tot_time) > 12:
        print("No")
    else:
        print("Yes")