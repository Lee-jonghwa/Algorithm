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