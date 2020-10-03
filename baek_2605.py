student = int(input())
num = list(map(int, input().split()))
# print(num)
init = []
for i in range(1, student+1):
    init.append(i)

for i in range(len(num)):
    t = num[i]
    j = i
    while t > 0:
        init[j-1], init[j] = init[j], init[j-1]
        t -= 1
        j -= 1
for i in range(len(init)):
    print(init[i], end=" ")