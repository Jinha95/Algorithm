def is_full():  #트리가 가득찼는지 확인
    return lastidx == N

def add(n):  #원소 추가
    global lastidx
    if is_full():
        print("트리가 포화상태임")
        return
    lastidx +=1
    tree[lastidx] = n

def inorder(idx):     #왼,부모,오른쪽 =>  LVR
    global result
    if idx <= lastidx:
        #왼쪽
        inorder(2*idx)     #왼쪽자식
        #현재노드 방문 (출력)
        result += [tree[idx]]
        #오른쪽
        inorder(2*idx + 1)     #오른쪽자식

T = 10
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)     #배열크기 지정
    lastidx = 0     #마지막에 들어온 원소가 위치할 인덱스

    #원소 넣기 : A,B,C,D...
    for _ in range(N):
        #원소 넣기
        li = list(map(str, input().split()))
        add(li[1])

    result = []

    inorder(1) #루트에서부터 중위순회
    print(f'#{t}', end=" ")
    for i in result:
        print(f'{i}', end="")
    print()


