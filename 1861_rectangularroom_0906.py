import sys
sys.stdin = open('1861_input.txt', 'r')

directions = [(0,1),(1,0),(-1,0),(0,-1)]


# dfs로 해보기

def dfs(y, x, lev, now_v): # 현재위치 y, x, lev가 움직인 방 갯수
    global max_v, now_min_v

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
        if arr[ny][nx] == arr[y][x] + 1: # 갈 수 있으면
            dfs(ny, nx, lev+1, now_v) # 갈 수 있으면 now_v는 유지됨

    # 종료 후 조건
    if max_v < lev:
        max_v = lev
        now_min_v = now_v
    elif lev == max_v:    # 그 중의 최소값
        if now_min_v > now_v:
            now_min_v = now_v


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    now_min_v = 1e9 # 최소 시작 방 번호
    max_v = 0 # 최대 이동 방 개수

    # 이동하는 방 수므로, 시작값은 1
    for y in range(N):
        for x in range(N):
            dfs(y,x,1,arr[y][x])

    print(f'#{tc} {now_min_v} {max_v}')



# 배열 크기 N^2
# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다
# 움직임이 최대인 방의 위치
# 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것 -> 역순으로
"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    visited = [0] * (N * N + 1) # 인덱스 맞추기(총 경우의수가 N^2)
    # 모두 서로 다른 수이므로 가능

    for y in range(N):
        for x in range(N):
            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                # 배열 넘어가면, continue
                if ny < 0 or ny >= N or nx < 0 or nx >= N: continue
                if arr[ny][nx] == arr[y][x] + 1: # 하나 차이 나면
                    visited[arr[y][x]] = 1
                    # 체크된 순간 다른 방향을 확인할 필요 없음
                    break


    # 이동 횟수
    cnt = 1
    max_v = 0
    # 시작 위치
    start = 0

    for i in range(N*N -1, -1, -1): # 작은 값이므로 큰값부터 돌아가기 필요
        if visited[i] == 1:
            cnt += 1

        else: # 옆으로 못 가면
            # 최대값 업데이트
            if max_v <= cnt: # 같은 경우가 있으니 =을 포함해야 함
                max_v = cnt
                start = i + 1  # 시작되는 값 업데이트(인덱스 맞추는 +1)
            # 카운트 초기화
            cnt = 1

    print(f'#{tc} {start} {max_v}')
"""
# 상하좌우에 있는 다른 방으로 이동할 수 있다.
# 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 -> dfs, 백트래킹
# 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.


# 내 옆에 나보다 1 큰 애가 있다면? -> 1로 저장

# 전체 배열을 순회하면서 확인
# 인접한 방의 순서가 현재 방보다 1 크면 visited 1체크
# 1이 크면 다음으로 갈 수 있다
# 다음으로 갈 수 있는 방이다라는 정보 저장
"""
directions = [(1,0),(0,1),(-1,0),(0,-1)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]

    visited = [0] * (N*N+1)

    # 전체를 순회하며
    # 상하좌우에 나보다 1이 크면 visited 체크
    for i in range(N):
        for j in range(N):
            for dy, dx in directions:
                ny = i + dy
                nx = j + dx
                if 0<=ny<N and 0<=nx<N:
                    # 옆이 1보다 크다면, 나는 움직일 수 있음을 표시
                    if arr[ny][nx] == arr[i][j] + 1:
                        visited[arr[i][j]] = 1
                        # 체크된 순간 다른방을 볼 필요가 없음
                        break

    # cnt: 하나씩 체크/ max_cnt: 결과값 / # 시작 위치
    cnt = 1
    max_cnt = start = 0

    for i in range(N*N -1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1 # 배열 안에서 나오도록
            cnt = 1
            # cnt 초기화

    print(f'#{tc} {start} {max_cnt}')
"""