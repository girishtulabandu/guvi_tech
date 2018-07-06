i=int(input("1 to start"))
l=[]
while (i==1):
    print("1 to push")
    print("2 to pop")
    k=int(input())
    if(k==1):
        j=int(input())
        l.append(j)
    elif(k==2):
        l.pop()
    else:
        break
    print("press 1 to continue")
    i=int(input())
print(l)


