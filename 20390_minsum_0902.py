# 방향 오른쪽, 아래
dir = [(0, 1), (1, 0)]

def dfs(x, y, sum_v):
    global min_sum

    if x == N - 1 and y == N - 1: # 오른쪽 아래 끝
        min_sum = min(min_sum, sum_v)
        return

    if sum_v >= min_sum:
        return # 가지치기

    # # 오른쪽으로 이동
    # if y < N - 1:
    #     dfs(x, y + 1, sum_v + arr[x][y + 1])
    #
    # # 왼쪽으로 이동
    # if x < N - 1:
    #     dfs(x + 1, y, sum_v + arr[x + 1][y])
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, sum_v + arr[nx][ny])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = float('inf')
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')


"""
directions = [(1,0), (0,1)]

def check(now_y, now_x, end_y, end_x, sum_v):
    global min_v

    if sum_v > min_v:
        return

    if now_y == end_y and now_x == end_x: # 도착하면
        if min_v > sum_v:
            min_v = sum_v
        return

    for dy,dx in directions:
        ny, nx = now_y + dy, now_x + dx
        if 0 <= ny < N and 0 <= nx < N and used[ny][nx] == 0:
            used[ny][nx] = 1
            check(ny, nx, end_y, end_x, sum_v + arr[ny][nx])
            used[ny][nx] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*N for _ in range(N)]
    min_v = 10000

    check(0,0,N-1,N-1,arr[0][0])
    print(f'#{tc} {min_v}')
"""
