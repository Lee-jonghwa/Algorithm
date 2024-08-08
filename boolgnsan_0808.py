def redm(y, x, N):
    visited[y][x] = 1
    if y == gy and x == gx:
        return 1
    if a[y][x] == 1:
        return
    else:
        for dy, dx in [(-1,0),(0,-1),(1,0),(0,1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and a[ny][nx] == 0:
                if redm(ny, nx, N):
                    return 1
    return 0

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

sy, sx = 0, 0
gy, gx = N-1, N-1

visited = [[0]*N for _ in range(N)]

print(redm(sy,sx,N))