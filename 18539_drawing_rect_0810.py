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
