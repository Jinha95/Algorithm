# import heapq
#
# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     info = list(map(int, input().split()))
#     heapq.heapify(info)
#     info = [0] + info
#     sum = 0
#     b = N
#     while b//2 != 0:
#         sum += info[b//2]
#         b = b // 2
#     print(f'#{t} {sum}')
#     print(info)
import heapq
T = int(input())
for t in range(1, T+1):
    N = int(input())
    info = list(map(int, input().split()))
    heap = []
    for i in info:
        heapq.heappush(heap, i)
    heap = [0] + heap
    total = 0
    b = N
    while b//2 != 0:
        total += heap[b//2]
        b = b // 2
    print(f'#{t} {total}')