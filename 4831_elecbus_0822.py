# 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서
# 0번에서 출발해 N번까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
# M개의 정류장 번호
# 종점에 도착할 수 없는 경우는 0

def elecbus(K, N, busstops):
    bus_now = 0  # 버스 위치
    cnt = 0
    while bus_now < N:  # 버스가 종점에 도착할때까지 반복
        bus_now += K  # 최대한으로 전진
        if bus_now >= N:  # 종점 도착하면
            return cnt  # 넘어가면 cnt 제출
        else:
            for i in range(bus_now, bus_now - K, -1):  # 지금부터 이전까지
                if busstops[i] == 1:
                    bus_now = i  # 인덱스 반영
                    cnt += 1
                    break
            else:
                return 0
    return -1 # 돌때까지 못하면


T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    recharger = list(map(int, input().split()))
    busstops = [0 for i in range(N)]
    for i in recharger:
        busstops[i] = 1
    result = elecbus(K,N,busstops)
    print(f'#{tc} {result}')





