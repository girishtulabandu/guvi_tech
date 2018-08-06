n,q=input().split()
n=int(n)
q=int(q)
a=input().split()
l=[]
for i in range(n):
    l.append(int(a[i]))
arr=[]
for i in range(q):
    b=input().split()
    for i in range(2):
        arr.append(int(b[i]))
for i in range(0,len(arr),2):
    min=999
    for j in range(arr[i]-1,arr[i+1]):
        if(l[j]<=min):
            min=l[j]
    print(min)
    
    
