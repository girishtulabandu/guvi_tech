s=input()
strlist=list(s)
analis=list("dhoni")
count=0
if(len(strlist)!=5):
    count=10
else:
    for i in range(5):
        for j in range(5):
            if(strlist[i]==analis[j]):
                count=count+1
if(count==5):
    print("yes")
else:
    print("no")
