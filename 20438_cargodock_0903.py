def Dok(arr):
    # 종료 시간 기준으로 빠른것 부터 정렬
    arr.sort(key=lambda x: x[1])
    end = 0  # 마지막 작업 끝난 시간
    cnt = 0  # 화물차 수

    for s, e in arr:
        # 작업 수행 했을 떄
        if s >= end:
            end = e
            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = Dok(arr)
    print(f'#{tc} {result}')


# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면, 최대 몇 대의 화물차가 이용할 수 있는지
# 작업 시작 시간과 완료 시간
# 앞 작업의 종료와 동시에 다음 작업을 시작할 수 있다.
# 예를 들어 앞 작업의 종료 시간이 5시면 다음 작업의 시작 시간은 5시부터 가능
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int,input().split())) for _ in range(N)]
    arr.sort(key= lambda x:x[1])

    cnt = 0
    target_time = 24
    now_time = 0 # 현재 시각
    for i in range(N): # 모든 경우에 대해서
        s, e = arr[i][0], arr[i][1]

        # 지금 시각보다 크거나 같으면
        if s >= now_time:
            cnt += 1
            # 끝나는 시간으로 ㅈ정
            now_time = e

    print(f'#{tc} {cnt}')
"""