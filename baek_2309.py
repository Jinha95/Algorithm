talls = []
for _ in range(9):
    tall = int(input())
    talls.append(tall)
# print(talls)
sumtall = sum(talls)
# print(sumtall)
for i in range(8):
    for j in range(i+1, 9):
        if sumtall - talls[i] - talls[j] == 100:
            a, b = talls[i], talls[j]
            break
talls.remove(a)
talls.remove(b)
# print(talls)
talls.sort()
for i in range(len(talls)):
    print(talls[i])