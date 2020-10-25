def fibo(number):
    result = [] # declare list
    a, b = 0, 1

    while a < number: # looping with while
        result.append(a)
        a, b = b, a+b
    
    return result # return list type variable

print(fibo(5))