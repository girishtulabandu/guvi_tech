s=input()
real=list(s)
check=[]
count=0
for i in range(97,123):
    check.append(chr(i))
for i in range(len(check)):
    for j in range(len(real)):
        if(check[i]==real[j]):
            count+=1
if(count>=26):
    print("yes")
else:
    print("no")
