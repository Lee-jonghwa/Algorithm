def ocello(put_s, arr, N, M):
    # 기본 돌 두기
    arr[N // 2][N // 2] = 2    # 백돌 2
    arr[N // 2 - 1][N // 2 - 1] = 2

    arr[N // 2 - 1][N // 2] = 1    # 흑돌 1
    arr[N // 2][N // 2 - 1] = 1

    # 방향 8개 모두 탐색
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for i in range(M):  # 횟수 동안
        a, b, color = put_s[i]    # 좌표와 색 출력
        x, y = a - 1, b - 1 # 인덱스 맞추기
        arr[y][x] = color       # 돌 놓기

        for dy, dx in directions:
            stones_to_flip = []  # 뒤집을 자리 추가
            for k in range(1, N):  # 제자리는 어차피 있으므로
                ny, nx = y + dy * k, x + dx * k

                # 배열을 벗어나지 않는 선에서
                if 0 <= ny < N and 0 <= nx < N:
                    if arr[ny][nx] == 0:
                        break # 즉시 중지

                    #  색이 같은 부분을 발견했을 떄
                    elif arr[ny][nx] == color:
                        if stones_to_flip: # 뒤집을 돌 있으면
                            for f_y, f_x in stones_to_flip:
                                arr[f_y][f_x] = color

                    else: # 색이 다른 돌 발견하면
                        stones_to_flip.append(f_y,f_x)# 후보에 추가
                else: # 배열을 벗어나면
                    break # 넘기기

    blacks = 0
    whites = 0

    for i in range(N): # 게임판을 순회해서
        for j in range(N):
            if arr[i][j] == 1:
                blacks += 1
            elif arr[i][j] == 2:
                whites += 1

    return blacks, whites


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 보드의 한 변의 길이 M:돌을 놓는 횟수
    arr = [[0]*N for _ in range(N)] # 보드 판
    put_s = [list(map(int, input().split())) for _ in range(M)] # 돌 놓는 경우의 수
    result = ocello(put_s, arr, N, M)
    print(f"#{tc}",*result)