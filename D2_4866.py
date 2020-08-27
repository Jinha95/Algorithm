T = int(input())
for t in range(1, T+1):
    li = list(map(str, input()))
    result = []
    result1 = True
    for i in range(len(li)):
        if li[i] == '(' or li[i] == '{':
            result.append(li[i])
        elif li[i] == ')' or li[i] == '}':
            if len(result) == 0:
                result1 = False
                break
            else:
                a = result.pop()
                if a == '(' and li[i] == '}':
                    result1 = False
                    break
                elif a == '{' and li[i] == ')':
                    result1 = False
                    break

    if result1 == True and len(result) == 0:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')







# def check(arr):
#     for i in range(len(arr)):
#         if arr[i] == '(':   # 왼쪽 괄호면 push
#             stack.append(arr[i])
#         elif arr[i] == ')':   # 오른쪽 괄호면 pop하고 비교
#             if len(stack) == 0:  # pop할땐 항상 비어있는지 확인
#                 return False
#             else:
#                 stack.pop()
#     if stack : return False
#     else : return True
#
# stack = []   # 빈 스택을 하나 만들어 줘야 함
# arr = "()()((()))"
# print(check(arr))
