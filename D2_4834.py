T = int(input())
for i in range(1, T+1) :
    N = int(input())
    ai = input()
    a = list(ai)
    c = [0 for i in range(10)]
    for j in range(len(a)):
        c[int(a[j])] += 1
    max = c[0]
    num = 0
    for j in range(len(c)):
        if c[j] >= max :
            max = c[j]
            num = j
    print(f'#{i} {num} {max}')


