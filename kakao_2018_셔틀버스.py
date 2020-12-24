def changeprint(time):
    minu = time % 60
    hour = time // 60
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    if minu < 10:
        minu = '0' + str(minu)
    else:
        minu = str(minu)
    return hour + ':' + minu


def solution(n, t, m, timetable):
    # 사람이 언제 오나
    new_timetable = []
    for i in timetable:
        s = i.replace(':', '')
        s = int(s[:-2]) * 60 + int(s[-2:])
        new_timetable.append(s)
    new_timetable.sort()
    # print(f'new_timetable{tc}: {new_timetable}')

    # 버스가 언제오나
    bustime = []
    first_time = 540
    for i in range(n):
        bustime.append(first_time)
        first_time += t
    # print(f'bustime{tc}: {bustime}')

    # 크루원들이 오는 시간중에 일단 중복을 모두 제거하고, 그 시간과 같은것, -1한것, 버스시간 모두를 합한 리스트가 나올 수 있는 경우의 수
    possible = []
    for i in list(set(new_timetable)):
        possible.append(i)
        possible.append(i - 1)
    possible += bustime
    possible = list(set(possible))
    possible.sort()
    # print(f'possible{tc}: {possible}')

    # 검사 리스트를 만들어서 possible을 돌며 검사하고 가능하면 1 불가능이면 그대로 0
    new_timetable += [999999]
    visit = [0] * len(possible)
    for i in range(len(possible)):
        for j in range(len(new_timetable)):
            if possible[i] < new_timetable[j]:
                newnew_timetable = new_timetable[:j] + ['a'] + new_timetable[j:]
                break
        newnew_timetable.pop(-1)
        # print(f'newnewtimetable: {newnew_timetable}')
        # print(f'a는 {possible[i]}')
        if len(newnew_timetable) <= m:
            return changeprint(bustime[-1])
        else:
            # newnew_timetable의 순서대로 버스를 탈건데 'a'가 탈 수 있는가
            k = 0  # k 번째 크루원
            z = 0  # z 번째 버스
            seat = list([0] * m for _ in range(n))
            while True:
                if k > len(newnew_timetable) - 1:
                    break
                if z > len(bustime) - 1:
                    break
                if 0 in seat[z]:  # z 번째 버스에 자리가 있다면, 자리채우고 다음사람, 버스그대로
                    if newnew_timetable[k] == 'a' and possible[i] <= bustime[z]:
                        seat[z].append('a')
                        seat[z].remove(0)
                        k += 1
                        visit[i] = 1
                        break
                    elif newnew_timetable[k] != 'a' and newnew_timetable[k] <= bustime[z]:
                        seat[z].append(newnew_timetable[k])
                        seat[z].remove(0)
                        k += 1
                    elif newnew_timetable[k] != 'a' and newnew_timetable[k] > bustime[z]:
                        z += 1
                    elif newnew_timetable[k] == 'a' and possible[i] > bustime[z]:
                        z += 1
                else:  # z번째 버스에 자리가 없다면, 사람그대로 다음버스로
                    z += 1
    # print(f'visit{tc}: {visit}')
    for i in range(len(visit) - 1, -1, -1):
        if visit[i] == 1:
            return changeprint(possible[i])