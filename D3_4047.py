T = int(input())
for t in range(1, T+1):
    info = input()
    # 정보를 받아오는데, 3자리씩 띄어서 정보를 저장
    info = [info[q:q + 3] for q in range(0, len(info), 3)]
    # print(info)
    S = [0] * 13
    D = [0] * 13
    H = [0] * 13
    C = [0] * 13
    # print(int(info[1][1:3]))
    for i in info:
        if i[0] == 'S':
            S[int(i[1:3])-1] += 1
        elif i[0] == 'D':
            D[int(i[1:3])-1] += 1
        elif i[0] == 'H':
            H[int(i[1:3])-1] += 1
        elif i[0] == 'C':
            C[int(i[1:3])-1] += 1
    if max(S) > 1 or max(D) > 1 or max(H) > 1 or max(C) > 1:
        print(f'#{t} ERROR')
    else:
        Sresult = S.count(0)
        Dresult = D.count(0)
        Hresult = H.count(0)
        Cresult = C.count(0)
        print(f'#{t} {Sresult} {Dresult} {Hresult} {Cresult}')