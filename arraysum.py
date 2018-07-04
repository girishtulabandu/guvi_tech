N=int(input())
k=int(input())
add=0
b=list(range(1,N+1))
for i in range(k):
    add=add+b[i]
print(add)
