def find_start(arr, N):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return y, x

def farest(arr, N, sy, sx):
    max_v = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                sum_v = ((sy - y)**2 + (sx - x)**2)**0.5
                if max_v < sum_v:
                    max_v = sum_v
    if int(max_v) < max_v < int(max_v) + 1:  # 중계기의 범위가 집 보다는 넓어야함
        return int(max_v) + 1
    else:
        return int(max_v)



T = int(input())
for tc in range(1, T+1):
    N = int(input()) + 1 # 전체가 N+1
    arr = [list(map(int, input().split())) for _ in range(N)] # N*N 배열
    sy, sx = find_start(arr, N)
    result = farest(arr, N, sy, sx)
    print(f'#{tc} {result}')
