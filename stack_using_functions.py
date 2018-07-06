i=int(input("1 to start"))
l=[]
def pushs(j):
    l.append(j)
    return (l)

def pops():
    if(l==[]):
        print("list is empty,can't pop")
    else:
        l.pop()
        return (l)

while (i==1):
    print("1 to push")
    print("2 to pop")
    k=int(input())
    if(k==1):
        j=int(input())
        pushs(j)
    elif(k==2):
        pops()
    else:
        break
    print("press 1 to continue 2 to display")
    i=int(input())
print(l)

    
