import  math
n=int(input())

if(n==2):
    print("yes")
elif(n>2):
    square_root=int(math.sqrt(n))
    for i in range(2,square_root+1):
        if(n%i==0):
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
