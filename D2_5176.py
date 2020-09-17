def inorder(idx):     #왼,부모,오른쪽 =>  LVR
    global result
    global lastidx
    if idx <= N:
        #왼쪽
        inorder(2*idx)     #왼쪽자식
        #현재노드 방문 (출력)
        lastidx += 1
        tree[idx] = lastidx
        #오른쪽
        inorder(2*idx + 1)     #오른쪽자식

T = int(input())
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)     #배열크기 지정
    lastidx = 0     #마지막에 들어온 원소가 위치할 인덱스

    inorder(1)

    print(f'#{t} {tree[1]} {tree[N//2]}')