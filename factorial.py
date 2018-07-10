r=int(input())
def factorial(r):
    if(r==0):
        return 1
    else:
        return r*factorial(r-1)

print(factorial(r))
