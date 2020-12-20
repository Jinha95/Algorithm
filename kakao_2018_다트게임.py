def solution(dartResult):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    score = []
    n = ""
    for i in dartResult:
        if i in num:
            n += i
        elif i == 'S':
            score.append(int(n) ** 1)
            n = ""
        elif i == 'D':
            score.append(int(n) ** 2)
            n = ""
        elif i == 'T':
            score.append(int(n) ** 3)
            n = ""
        elif i == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2
        elif i == '#':
            score[-1] *= -1

    answer = sum(score)
    return answer