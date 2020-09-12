T = int(input())
for t in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))

    #사용한 점수는 1로 바꿔. 0은 자동사용함. visit은 최고점수만큼 크기 있음
    visit = [1] + [0]*sum(info)
    # 0 기본
    result = [0]

    for i in info:
        # 이게 result 를 사용하면 중복될 수가 있음. 그래서 바로 직전까지 추가된 result만 가지고 실행
        # 아마도 nochangeresult = result 했을때 오류났던건 id값? 이 같아서? 모름 쨋든 오류남
        # 그래서 요소로 받아옴
        nochangeresult = result[:]
        for j in nochangeresult:
            if visit[i+j] == 0:
                visit[i+j] = 1
                result.append(i+j)
    sol = len(result)
    print(f'#{t} {sol}')