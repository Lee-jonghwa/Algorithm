# 5,000 개 정류장
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N
# N개의 줄의 i번째 줄에는 두 정수 Ai, Bi
# 다음 줄에는 하나의 정수 P
# 다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj

def ssbus():
    bus_stops = [0] * 5001
    for bus in buses:
        for i in range(bus[0], bus[1] + 1):
            bus_stops[i] += 1
    res_lst = []
    for j in tar:
        res_lst.append(bus_stops[j])
    return res_lst


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    buses = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    tar = [int(input()) for _ in range(P)]
    result = ssbus()
    print(f'#{tc}', *result)

"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001

    for i in range(N):
        Ai, Bi = map(int, input().split())

        for j in range(Ai, Bi + 1):
            bus_stop[j] += 1

    P = int(input())
    result = []
    for k in range(P):
        Cj = int(input())
        result.append(bus_stop[Cj])
    print(f'#{tc}', *result)
"""

"""
# Ai: 시점, Bj: 종점
# 이상이고, 이하인 정류장을 다니는 조건 --> 왔다갔다 하는 경우는 큰 경우와 작은 경우 모두 생각 필요
# 각 정류장에 몇 개의 버스 노선에 다니는지 계산


# N: 버스 노선 수
# a, b: 버스 출발 및 종점(총 N개)
# P: 버스정류장의 개수
# c: 지나는 버스를 구해야하는 버스정류장  --> 1~P까지가 아님


''' # 추가 테스트 케이스 고려해보기
2
2
1 3
2 5
5
1
2
3
4
5
2
1 3
2 5
5
1
2
3
4
5

'''


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # # N개의 노선 정보를 모두 읽어 놓고 처리
    # bus_w = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 5001  # 1 ~ 5000번까지 지나간 길 처리 할 것 초기화
    # --> P를 기준으로 하지 말고 전체를 기준으로 할 것

    # N 개의 노선 정보를 읽을 때마다 처리
    for _ in range(N):
        # Ai(시점) -> Bi(종점), Ai <= Bi
        A, B = map(int, input().split())
        for i in range(A, B+1): # 시작점에서 종점까지, 1 ≤ Ai ≤ Bi ≤ 5,000
            cnt[i] += 1


    P = int(input())  # 노선수를 출력할 버스 정류장의 수
    # 정류장의 수를 읽어놓고 처리
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=" ",)
    for j in busstop:
        # 끝에 있는 빈칸은 자동으로 무시가 됨
        print(cnt[j], end=" ")
        # 하지만 같은 줄에 다른 케이스가 있으면 안 됨
    print()



# 다른 idea
# P를 읽으면서 -> 각 버스 시점과 종점 사이에 노선이 포함되어 있나? + 1
"""