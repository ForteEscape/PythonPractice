def sum_number(num1, num2):
    return num1 + num2

def div_number(num1, num2): # expression of divide operator
    return num1 / num2

def getQuotient(num1, num2): # expression of divde quotient
    return num1 // num2

def getRemain(num1, num2):
    return num1 % num2

def getSquare(num1, num2): # expression of square operator
    return num1 ** num2

num1 = int(input())
num2 = int(input())

print(sum_number(num1, num2))
print(div_number(num1, num2))
print(getQuotient(num1, num2))
print(getRemain(num1, num2))
print(getSquare(num1, num2))