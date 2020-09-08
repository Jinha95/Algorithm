T = 10
for t in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    # print(visit)
    # 내려가는 N 먼저확인
    # 모두 확인하되 visit 안된 있는 애만 확인하면 된다.
    result = 0
    for i in range(N):
        for j in range(N):
            if table[j][i] == 1 and visit[j][i] == 0:
                visit[j][i] = 1
                # N 이라면?? 뭔가 있을때까지 계속 내려가야 되니까 while
                a = j
                while a < N-1:
                    # 점점 내려가다가 똑같은 N을 만나면? --> 그냥 무시하고 계속 내려감. 대신 만난 N은 검사를 안할거임
                    if table[a+1][i] == 1 and visit[a+1][i] == 0:
                        visit[a+1][i] = 1
                        a += 1
                    # 서로다른 S극을 만나면? --> 다음에 검사 안하게 visit에 체크하고, 결과값 하나 올리기.
                    elif table[a+1][i] == 2 and visit[a+1][i] == 0:
                        visit[a+1][i] = 1
                        result += 1
                        break # 그만 내려가기
                    # 아무것도 없다면? --> 0을 만난다면? 계속 내려가기
                    else:
                        a += 1
            elif table[j][i] == 2 and visit[j][i] == 0:
                visit[j][i] = 1
                b = j
                while b > 0:
                    if table[b - 1][i] == 2 and visit[b - 1][i] == 0:
                        visit[b - 1][i] = 1
                        b -= 1
                    elif table[b - 1][i] == 1 and visit[b - 1][i] == 0:
                        visit[b - 1][i] = 1
                        result += 1
                        break
                    else:
                        b -= 1
    print(f'#{t} {result}')


