T = int(input())
for tc in range(1, T+1):
    N = int(input()) + 1
    a = [list(map(int, input().split())) for _ in range(N)]
    mc = () # 중계기 좌표
    town = [] # 집 좌표
    for i in range(N):
        for j in range(N):
            if a[i][j] == 2:
                mc = i, j
            elif a[i][j] == 1:
                town.append((i, j))

    max_d2 = 0
    for y, x in town:
        d2 = (mc[0] - y)**2 + (mc[1] - x)**2
        if d2 > max_d2:
            max_d2 = d2
    r = max_d2**0.5
    if r > int(r):
        r = int(r) + 1
    else:
        r = int(r)
    print(f'#{tc} {r}')
