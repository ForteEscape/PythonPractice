# Week 2 제어흐름

## 1. if문
<pre>
<code>
x = int(input())

if x > 10:
    print("x is bigger than 10")
elif x < 0:
    print("x is smaller than 0")
elif x == 5:
    print("x is 5)
else:
    print(number)
</code>
</pre>

- else if의 역할을 elif 라는 축약어가 대신한다.

- 그 외 제어 측면에서 다른 점은 없다.

## 2. for문
<pre>
<code>
words = ['cat', 'window', 'car']

for index in words:
    print(index, len(index))
</code>
</pre>

- C-like한 언어에서 사용하는 포멧인 ```for(declare, option, in/decrease)```의 형식과는 다르게 ```for index in list``` 과 같은 형식이다.

- 이러한 방식에서 임의의 순서가 정해진 순열(list)를 순서대로 실행하도록 동작한다.

- 이러한 이터레이션(반복)을 숫자들의 시퀸스로 해야 할 필요가 있을 시에는 ```range()``` 함수를 사용한다.
    - ex) ```for index in range(5)``` 0~4까지 5번 반복한다.

- 이러한 ```range()``` 함수를 그냥 출력하려고 할 시 우리가 원하는대로 동작하지 않는다.(range(5)를 출력할 시 range(0, 5)가 출력된다.) range가 반환하는 객체는 이터러블(iterable) 객체라고 부르며 range의 경우에는 리스트처럼 동작한다.

- iterable object는 object의 member를 한 번에 하나씩 반환할 수 있는 객체를 일컫는다. 

<pre>
<code>
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')
</code>
</pre>

- break의 경우 C, JAVA등에서 배운 break문과 동일하게 동작한다.

- else의 경우 for - else문으로 for looping이 break문에 의해 끊어지지 않고 모두 반복된 이후 실행되는 구문을 담는 곳이다.

- continue 구문도 있으며 이 역시 C와 동일한 동작을 한다.

- 반복문에서 while, do - while문은 C와 동일한 형태, 동작을 하고 있다.

## 함수(function)
- 함수의 선언은 def로 시작하며 def functionName으로 선언할 수 있다.

<pre>
<code>
def comparator(num1, num2):
    return (num1 if num1 > num2 else num2)
</code>
</pre>

- 함수의 return문은 인터프리터가 알아서 반환형을 결정하여 돌려준다.

- 함수의 호출에서 parameter의 경우 Call by Value로 호출된다. 이때 값(value)는 언제나 객체의 값이 아니라 객체 참조(reference)이다.
    - 예를 들어 x = 10이라는 문장에서 x에 10이 대입되는 대입문으로 생각하지만 파이선에서는 그렇지 않다. 파이선에선 10이 들어있는 객체를 가리키는 변수 x로 해석할 수 있다. (C의 포인터와 유사한 개념이다.)