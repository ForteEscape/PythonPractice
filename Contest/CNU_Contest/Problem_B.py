import sys

Mbti_data = sys.stdin.readline().rstrip()
cnt = 0
N = int(sys.stdin.readline().rstrip())

for i in range(N):
    data = sys.stdin.readline().rstrip()

    if Mbti_data == data:
        cnt += 1

print(cnt)