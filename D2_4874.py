def cal(a, c, b):
    a = int(a)
    b = int(b)
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a // b

T = int(input())
for t in range(1, T+1):
    stack_result = input().split()
    stack_result.pop()
    stack = []
    # 후위연산 스택을 순회하면서 확인
    for i in stack_result:
        # 숫자라면 임시저장
        if '0' <= i <= '9':
            stack.append(i)
        else:
            if len(stack) < 2:
                print('#{} error'.format(t))
                break
            # 연산자면 2개를 꺼내서 계산한다.
            b = stack.pop()
            a = stack.pop()
            stack.append(cal(a, i, b))
    else:
        # 결과값 출력
        if len(stack) != 1:
            print('#{} error'.format(t))
            continue
        print('#{} {}'.format(t, stack[0]))