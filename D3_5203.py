def runn(player):
    global playerwin
    player.sort()
    a = list(set(player))
    for i in range(len(player)-2):
        if (player[i] == player[i+1] and player[i+1] == player[i+2]):
            playerwin = True
            break
    for i in range(len(a)):
        if (a[i] + 1 in a and a[i] + 2 in a):
            playerwin = True
            break
T = int(input())
for tc in range(1, T+1):
    li = list(map(int, input().split()))
    # print(li)
    player1 = []
    player2 = []
    playerwin = False
    for game in range(6):
        player1.append(li[game*2])
        player2.append(li[(game*2)+1])
        if game > 1:
            runn(player1)
            if playerwin == True:
                print(f'#{tc} 1')
                # print(player1)
                break
            runn(player2)
            if playerwin == True:
                print(f'#{tc} 2')
                # print(player2)
                break

    if playerwin == False:
        print(f'#{tc} 0')
        # print(player1)
        # print(player2)
