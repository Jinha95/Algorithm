def comb(n,r):  #n : 원소 인덱스, r : sel배열의 어디에 넣을지 (선택한 원소의 수)
    if r == N : #조합 다고름
        for i in range(len(sel)):
            print(sel[i], end= " ")
        print()
        return
    elif n >= len(arrr):
        return
    sel[r] = arrr[n]
    comb(n+1,r+1)   #r위치의 원소 선택한 경우
    comb(n+1,r)     #r위치의 원소 선택 안함.

while True:
    arr = list(map(int, input().split()))
    n = int(arr[0])
    if n == 0:
        break
    arrr = arr[1:]
    N = 6
    sel = [0] * N
    comb(0, 0)
    print()