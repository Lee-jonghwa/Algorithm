# 그릴 수 있는 최대 면적 사각형 갯수
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
