from itertools import combinations
import copy




dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def virus(x, y):
    global test
    if visit[x][y] == 0:
        visit[x][y] = 1
        if test[x][y] == 1:
            return
        else:
            test[x][y] = 2
            for l in range(4):
                nx = x + dx[l]
                ny = y + dy[l]
                if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0:
                    virus(nx, ny)


N, M = map(int, input().split())
li = []
for _ in range(N):
    lili = list(map(int, input().split()))
    li.append(lili)
# print(N)
# print(M)
# print(li)
# N x M 행렬이다. 으갸ㅑ갸갸갸ㅑ갸갸갸갸갹
# 바이러스는 상하좌우로 퍼져 나갈 수 있구, 벽 새로 3개 세운대
# 0은 빈칸, 1은 벽, 2는 바이러스
# 벽을 3개 세워서 바이러스를 최대한 안퍼지게 하고 안퍼진거 개수 최대?

# 어케할까 어케할까 어케할까
# 임의로 벽을 3개 세워서 걍 다 비겨ㅛ해보자
emempty = []
for i in range(len(li)):
    for j in range(len(li[i])):
        if li[i][j] == 0:
            empty = [i, j]
            emempty.append(empty)
#print(emempty)
# ememty는 빈공간의 좌표를 모두 가져옴. 여기서 3개를 뽑는 경우의 수로 가자
b = []
for i in list(combinations(emempty, 3)):
    j = list(i)
    b.append(j)

#print(b)

# 혹시 모르니까 복사해서 작업
test = copy.deepcopy(li)
# b 라는 배열에 3개의 좌표씩 묶여서 들가있음
# [[[0, 0], [0, 1], [0, 2]], [[0, 0], [0, 1], [0, 3]],  이런 형태
# 일단 바이러스 위치( 함수 시작점 따오기)
wherevirus = []
for i in range(len(test)):
    for j in range(len(test[i])):
        if test[i][j] == 2:
            wherevirus.append([i, j])
# print(wherevirus)

# 일단 벽을 세운다음에 비교해야됨
result = []
visit = list([0] * M for _ in range(N))
for i in range(len(b)):
    test[b[i][1][0]][b[i][1][1]] = 1
    test[b[i][2][0]][b[i][2][1]] = 1
    test[b[i][0][0]][b[i][0][1]] = 1

    # print(test)

    # 일단 다 바꿈. 이제 함수쓰자
    for j in range(len(wherevirus)):
        virus(wherevirus[j][0], wherevirus[j][1])
    # 다 바꿨으니까 계산하자
    # print(test)
    cnt = 0
    for k in range(len(test)):
        for z in range(len(test[k])):
            if test[k][z] == 0:
                cnt += 1
    result.append(cnt)
    test = copy.deepcopy(li)
    visit = list([0] * M for _ in range(N))

print(max(result))

# 다 하고 값만 저장하고 test는 초기화 해줄것
# # 여기서 경우를 나눠서 비교하자
# for i in range(len(b)):
#     # j 는 언제나 0, 1, 2
#     for j in range(len(b[i])):
#         test[b[i][j][0]][b[i][j][1]] = 1
#         # j 3번 돌면 다 1로 바뀌고
#     # 1로 바뀐 상태인 여기서 작업
#
#     virus(x, y, z)