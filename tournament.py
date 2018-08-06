n=int(input())
players=0
i=1
while(players!=n and players<n):
    players=2**i
    if(players==n):
        print("0")
        break
    if(players>n):
        players=2**(i-1)
        byes=n-players
        print(byes)
        break
    i+=1
    
