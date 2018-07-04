a=int(input())
b=int(input())
for n in range(a+1,b):
    temp=n
    arm=0
    if(n<=100000):
        while n>0:
            rem=n%10
            arm=arm+(rem**3)
            n=n//10
        if(arm==temp):
            print(arm)
    else:
        print("Invalid")

