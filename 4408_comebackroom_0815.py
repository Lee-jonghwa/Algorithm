# 윗방 - 복도 - 아랫방의 3 행의 리스트로 생각한다.
# 복도는 총 방갯수 // 2만큼의 인덱스를 가짐
# 어디로 가든 해당 칸의 복도를 지나가야하므로 매번 +1
# 결론적으로 가장 많이 지나간 복도를 return

def comebackroom():
    max_v = 0
    corridor = [0] * 201  # 입력값 인덱스 맞추기

    for room in rooms:
        if room[0] > room[1]: # 뒤에서 앞으로 이동
            for i in range((room[1] + 1) // 2, ((room[0] + 1) // 2) + 1): # 시작점부터 끝점까지
                corridor[i] += 1
        if room[0] < room[1]:  # 앞에서 뒤로 이동
            for j in range((room[0] + 1) // 2, ((room[1] + 1) // 2) + 1):
                corridor[j] += 1

    for k in corridor:
        if max_v < k:
            max_v = k

    return max_v


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야 할 학생 수
    rooms = [list(map(int, input().split())) for _ in range(N)]
    result = comebackroom()
    print(f'#{tc} {result}')

# 1 ~ 2나 1 ~ 3도 복도는 지나감
# 400개가 마주보므로 200개로 생각
# 겹치는 만큼 cnt 증가 -> 겹치는 구간 max
"""
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

"""