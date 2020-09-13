T = 10
for t in range(1, T+1):
    N = int(input())
    T =[[]]

    for i in range(1, N+1):
        T.append(list(input().split()))
        if len(T[i]) == 4:
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else:
            T[i][1] = int(T[i][1])

    def calc(v):
        if len(T[v]) == 2:
            return T[v][1]
        else:
            l = calc(T[v][2])
            r = calc(T[v][3])

            if T[v][1] == '+': return l + r
            elif T[v][1] == '-': return l - r
            elif T[v][1] == '*': return l * r
            else: return l / r
    print(f'#{t} {int(calc(1))}')