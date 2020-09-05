T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    a = M % N
    print(f'#{t} {li[M%N]}')