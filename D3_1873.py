T = int(input())
# 상하좌우
tank = ['^', 'v', '<', '>']
dir_dict = {'U':0, 'D':1, 'L':2, 'R':3}
# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search_tank():
    for i in range(H):
        for j in range(W):
            if board[i][j] in tank:
                return i, j, tank.index(board[i][j])

for tc in range(1, T+1):
    H, W = map(int, input().split())
    board = [list(map(str, input())) for _ in range(H)]
    # print(board)
    N = int(input())
    command = list(map(str, input()))
    # print(command)
    # 탱크위치 찾기
    r = c = dir = -1
    # for i in range(H):
    #     for j in range(W):
    #         if board[i][j] in tank:
    #             r = i
    #             c = j
    #             dir = tank.index(board[i][j])
    #             break
    #     if r != -1:
    #         break
    r, c, dir = search_tank()

    # 명령어 처리
    for cmd in command:
        # 폭탄 발사
        if cmd == 'S':
            nr = r + dr[dir]
            nc = c + dc[dir]
            while 0<=nr<H and 0<=nc<W:
                if board[nr][nc] == '#': break
                if board[nr][nc] == '*':
                    board[nr][nc] = '.'
                    break
                nr += dr[dir]
                nc += dc[dir]
        # 방향을 조종할때
        else:
            dir = dir_dict[cmd]
            board[r][c] = tank[dir]
            nr = r+dr[dir]
            nc = c+dc[dir]
            if 0<=nr<H and 0<=nc<W and board[nr][nc] == '.':
                board[nr][nc] = tank[dir]
                board[r][c] = '.'
                r, c = nr, nc
    print(f'#{tc}', end=" ")
    for i in range(H):
        print("".join(board[i]))