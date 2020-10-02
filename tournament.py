n = int(input('Enter a number: '))
players = 0
i = 1
while players < n:
    players = 2 ** i
    if players == n:
        print(0)
        break
    if players > n:
        players = 2 ** (i - 1)
        print(n - players)
        break
    i += 1
