n,k=input().split()
if(n.isdigit() and k.isdigit()):
    n=int(n)
    k=int(k)
    if(k==1):
        print("1 2")
    else:
        print("1 "+str(n-k))
    
