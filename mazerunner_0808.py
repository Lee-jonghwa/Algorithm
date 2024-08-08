def maze():
    while stack:
        y, x = stack.pop()
        arr[y][x] = -1 # 지나간 길 표시
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 3:
                    return 1 # 도착하면 1
                elif arr[ny][nx] == 0:
                    stack.append((ny, nx))

    return 0 # 도착점 못 찾으면 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)] # 미로
    for y in range(N):
        for x in range(N):
            # 시작점 찾기
            if arr[y][x] == 2: #시작점
                stack = [(y, x)]
                break # 시작점을 찾았기 때문에 더 이상 탐색할 필요 없음
        break
    print()


'''
directions = [(-1,0), (0,-1), (1,0), (0,1)]

def fstart(N):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:
                return i, j
    return -1, -1

def mzrunner(y, x, N):
    visited[y][x] = 1
    if a[y][x] == 3:
        return 1
    else:
         for dy, dx in directions:
            ny = y + dy
            nx = y + dx
            if 0 <= ny < N and 0 <= nx < N and a[ny][nx] != 1 and visited[ny][nx] == 0:
                if mzrunner(ny, nx, N):
                    return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    sti, stj = fstart(N)
    print(f'#{tc} {mzrunner(sti, stj, N)}')
'''