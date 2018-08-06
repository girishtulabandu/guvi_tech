n,a,b=input().split()
n=int(n)
a=int(a)
b=int(b)
total=0
while(total!=n and total<n):
    total=total+a+b
if(total==n):
    print("YES")
else:
    print("NO")
