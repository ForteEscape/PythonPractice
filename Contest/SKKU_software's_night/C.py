import sys

T, K = map(int, sys.stdin.readline().split())
skills = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

H = int(sys.stdin.readline().rstrip())
head_price = list(map(int, sys.stdin.readline().split()))
head_status = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

B = int(sys.stdin.readline().rstrip())
body_price = list(map(int, sys.stdin.readline().split()))
body_status = [list(map(int, sys.stdin.readline().split())) for _ in range(B)]

P = int(sys.stdin.readline().rstrip())
pants_price = list(map(int, sys.stdin.readline().split()))
pants_status = [list(map(int, sys.stdin.readline().split())) for _ in range(P)]

price = head_price + body_price + pants_price

if T < min(price):
    print(0)
    exit(0)

head_status = []
