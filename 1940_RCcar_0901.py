# 0 : 현재 속도 유지
# 1 : 가속
# 2 : 감속

# 가속도의 단위는, m/s2 이며, 모두 양의 정수
#  N 초 동안 이동한 거리를 계산하는 프로그램

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dist = 0 # 이동 거리
    vel = 0
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        if arr[i][0] ==0:
            dist += vel # 지금 속도 그대로
        else:
            command, acc = arr[i][0],arr[i][1]
            # 1초에 command 1개
            if command == 1:
                vel += acc
                dist += vel
            elif command == 2:
                vel -= acc
                if vel < 0:
                    vel = 0
                dist += vel

    print(f'#{tc} {dist}')