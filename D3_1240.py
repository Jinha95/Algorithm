T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = []
    for _ in range(N):
        li.append(input())
    # print(li)
    for i in li:
        if int(i) != 0:
            a = i
            break
    # 한참 찾았네 이거 문제 잘못됨
    # 테스트케이스 2번 M 80이라면서 81개 넣어놔가지고 '0'*M 안먹힘. int(i)로 바꿈
    # print(a)
    # a가 암호코드 찾아낼놈임
    for i in range(M-1, -1, -1):
        if a[i] == '1':
            b = i
            break
    # print(b)
    # b는 암호코드 끝나는 마지막 숫자 인덱스임
    # 그럼 이제 뭐 찾을까 음 ㅇㅁ ㅇ믕ㅇㄴㅁㅇ
    # 숫자가 8자리니까 8*7 = 56개 사용이니까
    # 뽑아내자
    code = a[b-55:b+1]
    # print(code)
    # 오 됐다
    # 정보를 저장해주자
    smallcode = ['0001101', '0011001', '0010011', '0111101', '0100011',
                 '0110001', '0101111', '0111011', '0110111', '0001011']
    # 7개씩 잘라서 만들어
    cocode = []
    for i in range(0, len(code), 7):
        cocode.append(code[i:i+7])
    # print(cocode)
    # 됐군
    for i in range(len(cocode)):
        for j in range(len(smallcode)):
            if cocode[i] == smallcode[j]:
                cocode[i] = j
                break
    # print(cocode)
    if (((cocode[0] + cocode[2] + cocode[4] + cocode[6]) * 3) + cocode[1] + cocode[3] + cocode[5] + cocode[7]) % 10 == 0:
        print(f'#{tc} {sum(cocode)}')
    else:
        print(f'#{tc} 0')
