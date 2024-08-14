def find_start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def maze(sy, sx, N):
    # 준비
    queue = []  # 큐 생성
    visited = [[0] * N for _ in range(N)]  # visited 생성
    queue.append((sy, sx))  # 시작점 enqueue
    visited[sy][sx] = 1  # 시작점 방문표시
    # 처리
    while queue:    # queue가 있을 동안
        ty, tx = queue.pop(0)   # dequeue
        if arr[ty][tx] == 3:    # 도착지에 도달하면
            return visited[ty][tx] - 1 - 1# 도착했을 때의 갯수 반환(출발지점 -1 도착지점은 제외 하므로 -1)
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            wy, wx = ty + dy, tx + dx
            # 배열을 벗어나지 않고 방문하지 않은 요소들에 대해서, 벽이 아닌 요소들에 대해
            if 0 <= wy < N and 0 <= wx < N and visited[wy][wx] == 0 and arr[wy][wx] != 1:
                queue.append((wy, wx))# 해당 지점 enqueue
                visited[wy][wx] = visited[ty][tx] + 1# 방문표시, lev 표시
    return 0 # 경로가 없는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sy, sx = find_start(N)
    result = maze(sy, sx, N)
    print(f'#{tc} {result}')
















def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    # 준비
    visited = [[0]*N for _ in range(N)]
    queue = []          # queue 생성
    queue.append([sti,stj]) # 시작점 enqueue
    visited[sti][stj] = 1   # 시작점 enqueue 표시

    # 탐색
    while queue:
        ti, tj = queue.pop(0)  # dequeue
        if maze[ti][tj] == 3:  # 도착 시 - visit(t)
            # 사이에 있는 빈칸의 갯수 -> visited - 1
            return visited[ti][tj] - 1 - 1  # 출발지 위치는 항상 1, 경로의 빈칸 수
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 인접이고, 벽이 아니면, 미로를 벗어나지 않고
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi,wj])               #enqueue
                visited[wi][wj] = visited[ti][tj] + 1 # enqueue 표시
    return 0 # 도달 못하는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')