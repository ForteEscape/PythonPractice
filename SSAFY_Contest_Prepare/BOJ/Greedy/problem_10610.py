# 입력된 수의 구성을 유지하면서 가장 큰 수를 만드는 방법은 앞자리부터 가장 큰 자리의 숫자가 나오게 하면 된다.
# 수를 정렬시켜 만든 뒤 그 수가 30의 배수인지 확인한다.

N = list(input())
N.sort(reverse=True)

result = ''
for element in N:
    result += element

if int(result) % 30:
    print(-1)
else:
    print(result)
