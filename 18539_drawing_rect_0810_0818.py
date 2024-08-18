
# 특정 좌표를 기준으로, "우측 하단"의 방향으로 사각형을 그릴 수 있다. -> y 값이 더 크고 x값이 같거나 큼
# 왼쪽 상단 좌표의 값과 우측 하단 좌표의 값이 동일해야 한다.
# 크기의 게임판이 주어졌을 때, 최대 면적의 사각형을 규칙대로 그릴 수 있는 총 사각형의 개수

def max_rect(arr, N):
    cnt = 0
    max_v = 0

    for y in range(N-1): # 만족하려면 마지막 전행까지만 가야함
        for x in range(N):
            for i in range(y+1, N): # y보다 큰 값
                for j in range(x, N): # x와 같아도 됨
                    if arr[y][x] == arr[i][j]:
                        area = (i - y + 1) * (j - x + 1)
                        if max_v < area:
                            max_v = area
                            cnt = 0
                        if area == max_v:
                            cnt += 1

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 게임판의 크기 N
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 게임판

    result = max_rect(arr, N)
    print(f'#{tc} {result}')
"""
def cnt_max_square(arr):
    max_area = 0
    cnt = 0
    for i in range(N):  # 사각형 왼쪽 상단의 행
        for j in range(N):  # 사각형 왼쪽 상단의 열
            for k in range(i, N):  # 사각형 오른쪽 하단의 행
                for l in range(j, N):  # 사각형 오른쪽 하단의 열
                    # 왼쪽 상단과 오른쪽 하단의 값이 같으면 면적 계산
                    if arr[i][j] == arr[k][l]:
                        area = (k - i + 1) * (l - j + 1)
                        if area > max_area:
                            max_area = area
                            cnt = 1
                        elif area == max_area:  # 현재 면적과 최대면적이 같으면
                            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = cnt_max_square(arr)
    print(f'#{tc} {result}')
"""


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]
    max_lst = []
    max_v = 0
    cnt = 0
    for y1 in range(N):
        for x1 in range(N):
            for y2 in range(y1+1, N):
                for x2 in range(x1, N):
                    if a[y1][x1] == a[y2][x2] and y1 < y2 and x1 <= x2:
                        sum_v = (y2 - y1 + 1) * (x2 - x1 + 1)
                        max_lst.append(sum_v)
                        if max_v < sum_v:
                            max_v = sum_v
    for i in max_lst:
        if max_v == i:
            cnt += 1
    print(f'#{tc} {cnt}')

"""
