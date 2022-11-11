N = int(input())
switch = list(map(int, input().split()))
student = int(input())
student_data = []

for i in range(student):
    sex, number = map(int, input().split())
    student_data.append([sex, number])

for data in student_data:
    # 남학생 구현
    if data[0] == 1:
        tmp = data[1]
        coef = 1
        while tmp <= N:
            if switch[tmp - 1] == 1:
                switch[tmp - 1] = 0
            else:
                switch[tmp - 1] = 1

            coef += 1
            tmp = data[1] * coef
    # 여학생 구현
    else:
        coef = 1
        switch[data[1] - 1] = 0 if switch[data[1] - 1] == 1 else 1
        while True:
            if (data[1] - coef) - 1 < 0 or (data[1] + coef) - 1 >= N:
                break

            if switch[(data[1] - coef) - 1] != switch[(data[1] + coef) - 1]:
                break
            else:
                switch[(data[1] - coef) - 1] = 0 if switch[(data[1] - coef) - 1] == 1 else 1
                switch[(data[1] + coef) - 1] = 0 if switch[(data[1] + coef) - 1] == 1 else 1

            coef += 1

for i in range(N):
    if i > 0 and i % 20 == 0:
        print("")
    print(switch[i], end=' ')

