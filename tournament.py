n=int(input())
players=0
i=1
while(players!=n and players<n):
    players=2**i
    if(players==n):
        print(n-players)
        break
    if(players>n):
        players=2**(i-1)
        print(n-players)
        break
    i+=1
    
