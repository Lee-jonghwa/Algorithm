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

