n=int(input())
temp=n
arm=0
if(n<=100000):
    while n>0:
        rem=n%10
        arm=arm+(rem**3)
        n=n//10
    if(arm==temp):
        print("yes")
    else:
        print("no")
else:
    print("Invalid")
