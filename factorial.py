N=int(input())
if(N<=20):
    def factorial(N):
        if(N==0):
            return 1
        else:
            return N*factorial(N-1)
else:
    print("Given number should be less than or equal to 20")
print(factorial(N))

