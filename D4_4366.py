NOTATION = '0123456789ABCDEF'
def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

T = int(input())
for tc in range(1, T+1):
    num2 = input()
    num3 = input()

# 2진수를 경우 하나씩 해서 다 바꿔본다음 그걸 다 10 진수로 바꿔서 저장하고 그걸 다 3진수로 바꿔서 저장해라
# 그 3진수들을 가진 리스트를 다 돌면서
# for for 이중 포문으로 만약 걔랑 3진수 걔랑 같은 자리수의 숫자가 1개 뺴고 다 똑같다면 그 숫자 저장
    temp2 = num2
    # print(len(num2))
    # print(type(num2))
    # print(type(temp2))
    li = []
    for i in range(len(num2)):
        if num2[i] == '1':
            temp2 = temp2[0:i]+'0'+temp2[i+1:]
        else:
            temp2 = temp2[0:i]+'1'+temp2[i+1:]
        li.append(temp2)
        temp2 = num2
    # print(num2)
    # print(temp2)
    # print(li)
    # 2진수에서 10진수로
    for i in range(len(li)):
        b = int(li[i], 2)
        li[i] = b
    # print(li)
    # 10진수를 3진수로 바꾸기
    for i in range(len(li)):
        c = numeral_system(li[i], 3)
        li[i] = c
    # print(li)

    result = []
    for i in range(len(num3)):
        for j in range(len(li)):
            for k in range(len(li[j])):
                if num3[0:i]+'5'+num3[i+1:] == li[j][0:k]+'5'+li[j][k+1:]:
                    result.append(li[j])
                    break
            if len(result) != 0:
                break
        if len(result) != 0:
            break
    # print(result)
    reresult = 0

    for i in range(len(result[0])):
        reresult += int(result[0][i]) * (3 ** (len(result[0])-i-1))

    print(f'#{tc} {reresult}')




