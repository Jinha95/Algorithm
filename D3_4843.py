T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    # list 만들고 쭉 추가할것
    li = []
    # 하나씩 지워나갈거니까 길이가 1될떄까지 계속 반복
    while len(A) > 0:
        # 제일 큰수 찾고
        top = max(A)
        # A 리스트에서 지워버리고
        A.remove(top)
        # 새로운 list 에 추가하고
        li.append(top)
        # 최소 찾고
        bot = min(A)
        # A 리스트에서 지우고
        A.remove(bot)
        # 새로운 list 에 추가하고
        li.append(bot)
    # 결과를 10개 까지만 출력
    result = ' '.join(map(str, li[0:10]))

    print(f'#{t} {result}')