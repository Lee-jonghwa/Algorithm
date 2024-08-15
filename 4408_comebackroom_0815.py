# 1 ~ 2나 1 ~ 3도 복도는 지나감
# 400개가 마주보므로 200개로 생각
# 겹치는 만큼 cnt 증가 -> 겹치는 구간 max

def come_back_room(rooms):
    cnt = [0] * 201 #복도 리스트 (지나갈 때마다 + 1)

    # 방들을 지나가면서
    for room in rooms:
        # 시작점 도착점 초기화
        start = 0
        goal = 0
        if room[0] < room[1]: # 출발방 보다 도착방이 큰 경우
            start = (room[0] + 1) // 2 # 200 맞춰주기
            goal = (room[1] + 1) // 2
        else: # 출발방 보다 도착방이 작으면
            # 시작과 끝 바꿈
            goal = (room[0] + 1) // 2 # 200 맞춰주기
            start = (room[1] + 1) // 2

        for j in range(start, goal + 1): # 시작방에서 끝 방까지, # 바로 앞 방도 포함
            cnt[j] += 1 # 지나간 표시

    return max(cnt)

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 돌아가야 할 학생 수
    rooms = [list(map(int, input().split())) for _ in range(N)] # 이동하는 방들
    result = come_back_room(rooms)
    print(f'#{tc} {result}')