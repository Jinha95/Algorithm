T = int(input())
for t in range(1, T+1):
    n = list(input().split())
    A = list(input().split())

    dic = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    for a in A:
        dic[a] += 1

    print(f'#{t}')
    print('ZRO ' * dic['ZRO'] + 'ONE ' * dic['ONE'] + 'TWO ' * dic['TWO'] +
          'THR ' * dic['THR'] + 'FOR ' * dic['FOR'] + 'FIV ' * dic['FIV'] +
          'SIX ' * dic['SIX'] + 'SVN ' * dic['SVN'] + 'EGT ' * dic['EGT'] + 'NIN ' * dic['NIN'])