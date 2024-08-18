# M초의 시간을 들이면 K개의 붕어빵
# 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별

# 세 자연수 N, M, K가 공백으로 구분되어 주어진다.
# 두 번째 줄에는 N개의 정수가 공백으로 구분되어 주어지며,


def isboong(N, M, K, buyers):
    for i in range(N):
        boongs = (buyers[i]//M) * K - i  # 지금까지 생산한 양 - 이전 손님이 먹은 양
        if boongs < 1: # 바이어 왔을 때 붕어빵이 없으면
            return "Impossible"
    return "Possible"

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    buyers = list(map(int, input().split()))
    buyers.sort()
    result = isboong(N, M, K, buyers)
    print(f'#{tc} {result}')

"""
# 붕어빵을 제공할 수 있으면 “Possible”을, 아니라면 “Impossible”

def shooboong(sec, N, M, K):
    sec.sort()

    for i in range(N):  # 손님이 다 올 때까지
        # i 번째 손님이 왔을 때 까지 있는 붕어빵
        available_boongs = (sec[i] // M) * K - i

        # 붕어빵이 부족하면
        if available_boongs < 1:
            return "Impossible"

    # 다 줄 수 있으면
    return "Possible"


T = int(input())
for tc in range(1, T+1):
    # N: 손님 수, M: 붕어빵 만드는 시간, K: 만들어지는 붕어빵 수
    N, M, K = map(int, input().split())
    # 만드는 시간
    sec = list(map(int, input().split()))
    result = shooboong(sec, N, M, K)
    print(f'#{tc} {result}')

"""
