def fivestone(N, arr):
    cnt = 0
    # 가로가 같으면
    for y in range(N):
        h = 0 # 가로 칸의 수
        for x in range(N):
            # 대각선
            if arr[y][x] == 'o': # 돌 놓여있는 자리에 대해서
                h += 1
            if arr[y][x] == '.' or y == N - 1: # 돌 없거나 행 끝에 도달
                if h >= 5:
                    cnt += 1
                h = 0


    # 세로가 같으면
    for x in range(N):
        v = 0
        for y in range(N):
            if arr[y][x] == 'o':  # 돌 놓여있는 자리에 대해서
                v += 1
            if arr[y][x] == '.' or x == N - 1:  # 돌 없거나 열 끝에 도달
                if v >= 5:
                    cnt += 1
                v = 0
    return cnt

    # 세로가 같으면
    # 오른쪽 아래로 대각선
    # 왼쪽 아래로 대각선

    # 못 찾으면
    print(stone_loc)
    return "NO"



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = fivestone(N, arr)
    print(f'#{tc} {result}')