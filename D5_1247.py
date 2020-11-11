from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lili = list(map(int, input().split()))
    company = lili[:2]
    home = lili[2:4]
    customer = []
    li = []
    for i in range(4, (2*N)+3, 2):
        li.append(lili[i])
        li.append(lili[i+1])
        customer.append(li)
        li = []

    per = permutations(customer)
    result = 10000000000
    for i in per:
        start = company
        reresult = 0
        for j in i:
            reresult += abs(j[0]-start[0]) + abs(j[1]-start[1])
            start = j
            if reresult > result:
                break
        reresult += abs(home[0]-start[0]) + abs(home[1]-start[1])
        if reresult < result:
            result = reresult
    print(f'#{tc} {result}')
