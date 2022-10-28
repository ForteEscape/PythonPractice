import sys

N = int(sys.stdin.readline().rstrip())
data = []
w, w_idx = 0, 0
h, h_idx = 0, 0

for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    data.append([direction, length])

for i in range(len(data)):
    if data[i][0] == 1 or data[i][0] == 2:
        if w < data[i][1]:
            w = data[i][1]
            w_idx = i
    elif data[i][0] == 3 or data[i][0] == 4:
        if h < data[i][1]:
            h = data[i][1]
            h_idx = i

sub_W = abs(data[(w_idx - 1) % 6][1] - data[(w_idx + 1) % 6][1])
sub_H = abs(data[(h_idx - 1) % 6][1] - data[(h_idx + 1) % 6][1])
print(((w * h) - (sub_W * sub_H)) * N)
