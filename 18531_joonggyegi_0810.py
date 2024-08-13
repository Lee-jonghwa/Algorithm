from math import ceil

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    houses = []  # 집의 위치의 좌표
    for i in range(N + 1):  # 좌표가 0 ~ N
        row = list(map(int, input().split()))
        for j in range(N + 1):
            if row[j] == 1:  # 집이면
                houses.append((i, j))
            elif row[j] == 2:  # 중계기면
                repeater = (i, j)

    max_r = 2  # 최소 2 이상이어야 함
    for y, x in houses:
        D = (y - repeater[0]) ** 2 + (x - repeater[1]) ** 2
        if max_r < D:
            max_r = D

    result = ceil(max_r ** 0.5)

    print(f'#{tc} {result}')
"""

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
"""