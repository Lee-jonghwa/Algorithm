import sys
sys.stdin = open('18567_input.txt','r')

# 오전
# 현재 농지가 빈 농지이고 로봇이 다음 농지로 이동할 수 있는 경우 씨를 심는다.
# 현재 농지가 빈 농지이고, 로봇이 다음 농지로 이동할 수 없을 경우 아무것도 하지 않고 현재 위치에서 머무른다.
# 현재 농지에 곡식이 열린 경우 수확을 한다. 수확을 하면 농지는 빈 농지가 된다.

# 오후

# 이동 가능한 곳은 빈 농지, 또는 곡식이 열린 농지이다. 산이거나 싹이 나는 농지인 경우 이동이 불가능하다
# 이동 가능한 곳이 여러 개인 경우, 로봇의 오른쪽, 앞쪽, 왼쪽, 뒤쪽의 순서로 가장 먼저인 이동 가능한 곳으로 이동한다
# 이동 가능한 곳이 없는 경우 로봇은 이동하지 않고 현재 위치에 머무른다.



#  M 일 까지 동작

# 로봇이 곡식을 가장 많이 수확할 수 있는 위치


# 싹이난 후 4 일 이후 곡식이 열림
# 해당 농지에 K번째로 싹이나면 3 +K일 이후에 곡식이 열린다.


"""
# 가는 방향: 오, 앞, 왼, 뒤 - > 바라보는 방향 기준으로 dy, dx 다름
# 바라보는 방향을 기준으로 오앞왼뒤 정리
moving_dir = {
    'left'  : [(-1,0,'up'),(0,-1,'left'),(1,0,'down'),(0,1,'right')],
    'up'    : [(0,1,'right'),(-1,0,'up'),(0,-1,'left'),(1,0,'down')],
    'right' : [(-1,0,'down'),(0,-1,'right'),(1,0,'up'),(0,1,'left')],
    'down'  : [(-1,0,'left'),(0,-1,'down'),(1,0,'right'),(0,1,'up')]
}

def grow_seeds():
    global seeds

    for i in range(N):
        for j in range(N):
            if seeds[i][j] == 0: continue
            seeds[i][j] += 1


def dfs(y, x, day, sum_v, directions):
    global max_v


    # 종료조건, 모든 곳을 순회했을 때
    if day == M:
        if max_v < sum_v:
            max_v = sum_v


    # 이동 조건
    # 로봇의 오른쪽, 앞쪽, 왼쪽, 뒤쪽의 순서로 가장 먼저인 이동 가능한 곳으로 이동한다

    for dy,dx,look_dir in directions:
        ny, nx  = y + dy, x + dx
        # 배열 벗어나면 x
        if ny >= N or ny < 0 or nx >= N or nx < 0: continue
        # 빈 자리라면
        if arr[ny][nx] == 0:
            # 씨 심음
            arr[ny][nx] = 2
            grow_seeds() # 이때까지 있었던 곳 + 1
            seeds[ny][nx] += 1
        # 수확할 수 있는 상황이라면
        if arr[ny][nx] == -1:


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_v = 0

    # 1이 아닌 모든 곳을 시작점으로 dfs -> 가지치기 조건 다양하게 하기
    for y in range(N):
        for x in range(N):
            for k in moving_dir:
                if arr[y][x] == 1: continue
                # 씨뿌리기 현황
                seeds = [[(0,0)] * N for _ in range(N)]
                dfs(y, x, 0, 0, moving_dir[k])
                
"""

moving_dir = {
    'left': [(-1, 0, 'up'), (0, -1, 'left'), (1, 0, 'down'), (0, 1, 'right')],
    'up': [(0, 1, 'right'), (-1, 0, 'up'), (0, -1, 'left'), (1, 0, 'down')],
    'right': [(1, 0, 'down'), (0, 1, 'right'), (-1, 0, 'up'), (0, -1, 'left')],
    'down': [(0, -1, 'left'), (1, 0, 'down'), (0, 1, 'right'), (-1, 0, 'up')]
}

def grow_seeds():
    global seeds, arr

    for i in range(N):
        for j in range(N):
            if seeds[i][j] > 0:  # 씨앗이 심어져 있으면 성장
                seeds[i][j] += 1
                # 4일 이상이면 곡식을 맺는다.
                if seeds[i][j] >= 4:
                    arr[i][j] = -1  # 수확 가능한 상태로 변경

def dfs(y, x, day, sum_v, directions, visited):
    global max_v

    if day == M:  # M일이 되면 종료
        max_v = max(max_v, sum_v)
        return

    # 오전 동작: 씨앗을 심거나 수확
    if arr[y][x] == 0:  # 빈 농지에 씨를 심는다
        arr[y][x] = 2  # 씨앗 심기
        seeds[y][x] = 1  # 씨가 심긴 날
    elif arr[y][x] == -1:  # 수확 가능한 상태
        sum_v += 1  # 수확량 증가
        arr[y][x] = 0  # 수확 후 빈 농지로

    # 방문 처리
    visited[y][x] = True

    # 씨앗 성장
    grow_seeds()

    # 오후 동작: 이동
    moved = False
    for dy, dx, look_dir in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and (arr[ny][nx] == 0 or arr[ny][nx] == -1):
            dfs(ny, nx, day + 1, sum_v, moving_dir[look_dir], visited)
            moved = True
            break  # 우선 순위 이동이므로 한 방향으로 이동했으면 나머지는 보지 않는다.

    # 이동할 곳이 없으면 제자리에 머문다
    if not moved:
        dfs(y, x, day + 1, sum_v, directions, visited)

    # 상태 복구
    visited[y][x] = False
    if arr[y][x] == 2:  # 씨앗 심은 상태 복구
        arr[y][x] = 0
    elif arr[y][x] == -1:  # 수확 상태 복구
        arr[y][x] = -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    # 로봇의 시작 지점과 방향
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 0:  # 농지인 경우에만 시작 가능
                for direction in moving_dir:
                    seeds = [[0] * N for _ in range(N)]  # 씨앗 상태 초기화
                    visited = [[False] * N for _ in range(N)]  # 방문 상태 초기화
                    dfs(y, x, 0, 0, moving_dir[direction], visited)

    print(f"#{tc} {max_v}")

