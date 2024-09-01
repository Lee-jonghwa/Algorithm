# 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째

days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}


T = int(input())
for tc in range(1, T+1):
    mon1, day1, mon2, day2 = map(int, input().split())

    new_day = 0
    for i in range(mon1, mon2): # 두 달 사이의 값을 더함
        new_day += days[i]

    new_day += day2 - day1 + 1

    print(f'#{tc} {new_day}')