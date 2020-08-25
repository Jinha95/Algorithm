T = int(input())
for i in range(1, T+1) :
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))

    result = []

    for j in range(N-M+1) : # 시작하는 인덱스
        c = 0               # 새로시작마다 c 초기화
        for k in range(M) :     # 몇개씩 더할건지
            a = ai[j+k]
            c += a
        result += [c] # 더한걸로 result 라는 리스트를 만들어 최대 최소를 찾아낸다.
    b = max(result) - min(result)
    print(f'#{i} {b}')
