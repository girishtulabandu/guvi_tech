n=int(input())
k=[]
for i in range(1,n):
    x=i
    l=[]
    while(x>0):
        rem=x%10
        x=x//10
        l.append(rem)
    sum=0
    for j in range(len(l)):
        sum=sum+l[j]
    sum=sum+i
    if(n==sum):
        k.append(i)
        
print(len(k))
for h in range(len(k)):
    print(k[h])
