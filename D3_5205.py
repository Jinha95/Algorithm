def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while i < high and arr[i] <= pivot :
            i+=1
        while j > low and arr[j] >= pivot:
            j-=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    n = len(arr)
    quickSort(arr,0,n-1)
    print(f'#{tc} {arr[n//2]}')