'''

# 출발지 정하기
def start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 출발 지점 2
                return i, j
    return -1, -1


def maze(arr, N, y1, x1):
    visited[y1][x1] = 1 # 흔적 남기기
    if arr[y1][x1] == 3: # 도착 구간 설정
        return 1
    else:
        for dy, dx in [(-1, 0), (0,-1), (1,0), (0,1)]: # 특정 지역에서 시작하므로, 배열 전체를 순회할 필요 없음
            ny, nx = y1 + dy, x1 + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 1 and visited[ny][nx] == 0: # 배열 이내에서, # 벽 벗어나지 않고 # 방문한 적 없는 곳
                if maze(arr, N, ny, nx): # 다음이 존재한다면
                    return 1
    return 0 # 다 돌아도 자리를 찾지 못한다면

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    y1, x1 = start(arr)
    result = maze(arr, N, y1, x1)
    print(f'#{tc} {result}')


'''

# 출발지 정하기
def fstart(arr, N): # 함수짤 때 가능하면 사용하는 요소 적을 건 다 적어보자
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 출발 지점 2
                return i, j
    return -1, -1


def maze(arr, N):
    start = fstart(arr, N)
    stack = [start] # 시작 지점이 정해져있으므로 start를 첫 요소로 추가
    while stack:
        y, x = stack.pop() # 현재 위치를 스택에서 팝
        arr[y][x] = -1 # 지나간 길 표시(다른 요소와 다르게 하기 주의) --> 가지치기
        for dy, dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3 : # 도착지에 도달하면
                    return 1
                elif arr[ny][nx] == 0: # elif 쓰는 이유: 2,1 등 다른요소 있음
                    stack.append((ny,nx)) # 통로면 스택에 추가
    return 0 # 찾지 못하면 0 리턴

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    result = maze(arr, N)
    print(f'#{tc} {result}')