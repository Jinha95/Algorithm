T = int(input())
for t in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    setstr1 = list(set(str1))
    setstr2 = list(set(str2))
    dic = {setstr1[i]:0 for i in range(len(setstr1))}

    for k in range(len(setstr1)):
        for j in str2:
            if j == setstr1[k]:
                dic[setstr1[k]] += 1

    maxdic = max(dic.values())

    print(f'#{t} {maxdic}')

