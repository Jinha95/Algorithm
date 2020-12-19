def solution(n, arr1, arr2):
    list1 = []
    for i in range(len(arr1)):
        j = 0
        num = [0] * n
        temp = arr1[i]
        while temp >= 1:
            j += 1
            num[n-j] = temp % 2
            temp = temp // 2
        list1.append(num)
    list2 = []
    for i in range(len(arr2)):
        j = 0
        num = [0] * n
        temp = arr2[i]
        while temp >= 1:
            j += 1
            num[n-j] = temp % 2
            temp = temp // 2
        list2.append(num)

    answer = [""]*n
    for i in range(n):
        for j in range(n):
            if list1[i][j] == 0 and list2[i][j] == 0:
                answer[i] += " "
            else:
                answer[i] += "#"
    return answer

# 2진수 쉽게 변환하는 방법
# value = 31
# num = format(value, 'b')
# print(num)

# 8진수 -> o
# 16진수 -> h
