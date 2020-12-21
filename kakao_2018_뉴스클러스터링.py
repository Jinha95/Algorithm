# def trash(li):
#     one = []
#     for i in range(len(li)):
#         if (65 <= ord(li[i][0]) < 91) and (65 <= ord(li[i][1]) < 90):
#             one.append(li[i])
#     return one

def solution(str1, str2):
    first = []
    second = []
    for i in range(len(str1) - 1):
        if (str1[i]+str1[i+1]).isalpha():
            first.append((str1[i] + str1[i + 1]).upper())
    for i in range(len(str2) - 1):
        if (str2[i] + str2[i + 1]).isalpha():
            second.append((str2[i] + str2[i + 1]).upper())

    print(first)
    print(second)
    #
    # first = trash(first)
    # second = trash(second)
    print(first)
    print(second)

    gyo = 0
    hap = len(first) + len(second)
    for i in second:
        if i in first:
            first.remove(i)
            gyo += 1
            # print(f'# {second}')

    print(gyo)
    print(hap)

    if hap == 0:
        return 65536
    elif hap == gyo:
        return 65536
    else:
        return int(((gyo / (hap - gyo)) * 65536))

str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2))