i=int(input())
l=[]
for x in range(i):
    j=input("")
    l.append(j)
b=[]
for i in range(len(l)):
    b.append(list(l[i]))
for k in range(1):
    for h in range(len(b[k])):
        if(b[k][h]==b[k+1][h]):
            print(b[k][h],end="")
        else:
            break
