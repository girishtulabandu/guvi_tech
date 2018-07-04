n=int(input())
q=int(input())
count=0
for i in range(n+1,q+1):
    for j in range(1,i+1):
        if(i%j==0):
            count=count+1
    if(count==2):
        print(i)
    count=0
    
    
