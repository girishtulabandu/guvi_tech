# r=int(input())
# def factorial(r):
#     if(r==0):
#         return 1
#     else:
#         return r*factorial(r-1)

# print(factorial(r))


import functools
factorial = lambda n: functools.reduce(lambda x, y: x * y, range(1, n+1))
num=int(input('Enter any Integer: '))
print(factorial(num))
