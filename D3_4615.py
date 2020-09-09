# 8방향 탐색을 위한 델타
# 가로, 세로, 대각선
dr =[-1,-1,0,1,1,1,0,-1]
dc =[0,1,1,1,0,-1,-1,-1]
'''
WBW  -> WWW
WBBW -> WWWW
WBWB -> WWWB
W BW -> W BW    (돌이 없으면 안함)
'''
def check(i,j,color):
    for k in range(8):      # 델타 길이 만큼 반복
        ni,nj = i + dr[k], j + dc[k]    # 탐색할 좌표 계산
        changeList =[]          # 변경할 좌표 리스트
        needtochange = False    # 변경여부를 저장

        # 한 방향으로 결정되면 쭉 나아가면서 돌을 변경할 준비
        while ni >= 0 and ni < N and nj >= 0 and nj < N:    # 보드안에서 반복
            if board[ni][nj] == 0:
                break
            if board[ni][nj] == color :     # 새로놓은 돌과 탐색한 돌색이 같으면
                needtochange = True         # 변경을 해야한다고 표시
                break
            else:
                changeList.append([ni,nj])  # 변경할 돌의 좌표 저장
                ni = ni + dr[k]
                nj = nj + dc[k]
        if needtochange and changeList:     # while반복종료후 바꿔야하고 바꿀게 있으면
            for c in changeList:
                board[c[0]][c[1]] = color


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 보드 크기
    # M : 게임 횟수
    board = [[0 for _ in range(N)] for _ in range(N)]
    center = N//2   # 중심선
    board[center-1][center-1] = 2
    board[center][center] = 2
    board[center-1][center] = 1
    board[center][center-1] = 1

    # for row in board:
    #     print(row)

    for k in range(M):
        j, i, color = map(int, input().split())   # 열,행,돌색을 입력
        board[i-1][j-1] = color   # 입력은 1로 시작됨 (인덱스 정보와 맵핑 필요)
        check(i-1,j-1,color)
    # 게임 종료후 돌 갯수 세기
    cnt_b = 0
    cnt_w = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 : cnt_b += 1
            elif board[i][j] == 2 : cnt_w += 1
    print("#{} {} {}".format(tc, cnt_b, cnt_w))
