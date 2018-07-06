n=int(input())
f=int(input())
l=[]
temp=n
count=0
while n>0:
    rem=n%10
    n=n//10
    count=count+1
for r in range(count):
    k=temp%10
    temp=temp//10
    l.append(k)

for j in range(f):
    l.pop()


for i in range(len(l)):
    for m in range(i+1,len(l)):
        if(l[i]>l[m]):
            (l[i],l[m])=(l[m],l[i])
        
for i in range(len(l)):
    print(l[i],end="")
