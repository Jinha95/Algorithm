s = input()
a = len(s)
cnt = 0
if s == ' ':
    print(0)
else :
    for i in range(1, a-1):
        if s[i] == ' ':
            cnt += 1
    print(cnt+1)