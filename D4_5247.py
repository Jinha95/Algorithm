# bfs로 푼다. 디큐 deque 데큐 뭥
# 왜 쓰는진 모르겠다 pop(0) 하면 될거같은데 안해봄 popleft랑 pop(0)가 뭐가 다른가가ㅏ아아아이이뤼ㅏㄴㅇ
from collections import deque
def operation(start):
    global cnt, visit
    q = deque()
    # q = []
    q.append((start, cnt))
    while len(q) > 0:
        start, cnt = q.popleft()
        # start, cnt = q.pop(0)
        if visit[start] == 0:
            visit[start] = 1
            if start == M:
                return cnt
            cnt += 1
            if 0 < start + 1 <= 1000000:
                q.append((start+1, cnt))
            if 0 < start - 1 <= 1000000:
                q.append((start-1, cnt))
            if 0 < start * 2 <= 1000000:
                q.append((start * 2, cnt))
            if 0 < start - 10 <= 1000000:
                q.append((start-10, cnt))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    visit = [0] * 1000001
    print(f'#{tc} {operation(N)}')

