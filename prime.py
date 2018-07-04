n=int(input())
count=0
if(n>0):
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count>2):
        print("no")
    else:
        print("yes")
else:
    print("Invalid")
