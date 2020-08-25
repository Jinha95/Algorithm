T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = []

    Garo = []
    for i in range(N):
        li = input()
        Garo.append(li)

        for i in range(len(li)-M+1):
            if li[i:M+i] == li[i:M+i][::-1]:
                result.append(li[i:M+i])

    Sero = []
    Sero_lst = ''
    for x in range(N):
        for y in Garo:
            Sero_lst += y[x]
        Sero.append(Sero_lst)
        Sero_lst =''

    for sero in Sero:
        for j in range(len(sero)-M+1):
            if sero[j:M+j] == sero[j:M+j][::-1]:
                result.append(sero[j:M+j])

    print(f'#{t} {result[0]}')