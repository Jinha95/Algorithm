def function(a, b):
    global result
    if(a >= 13):
        if(b < result):
            result = b
            return result
    else:
        function(a+1, b+d*month[a])
        function(a+1, b+m)
        function(a+3, b+m3)

T = int(input())
for tc in range(1, T+1):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    result = y
    function(1, 0)
    print(f'#{tc} {result}')