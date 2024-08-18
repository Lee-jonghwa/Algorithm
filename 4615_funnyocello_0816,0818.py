B = 1
W = 2

# 놓은 돌 기준으로 8방향 전진 --> 같은 색 만나면 멈추고 뒤집음
# 다른 색 만나면 후보로 둠
# 아무것도 없으면 넘어감

directions = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]

def occelo(put_stone):
    game = [[0] * N for _ in range(N)]
    # 초기 돌 놓기
    game[N // 2][N // 2] = W
    game[N // 2 - 1][N // 2 - 1] = W
    game[N // 2 - 1][N // 2] = B
    game[N // 2][N // 2 - 1] = B

    # 돌 세팅
    for x, y, color in put_stone:
        x, y = x - 1, y - 1 # 인덱스 맞추기
        game[y][x] = color


        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            flip_stone = []  # 뒤집을 돌

            while 0 <= ny < N and 0 <= nx < N and game[ny][nx] == 3 - color: # 다른 돌이면
                flip_stone.append((ny, nx))
                ny += dy
                nx += dx

            # 만났을 때 뒤집을 돌 있으면
            if 0 <= ny < N and 0 <= nx < N and game[ny][nx] == color and flip_stone:
                for y1, x1 in flip_stone:
                    game[y1][x1] = color

    bcnt = 0
    wcnt = 0
    for i in range(N):
        for j in range(N):
            if game[i][j] == B:
                bcnt += 1
            if game[i][j] == W:
                wcnt += 1
    return bcnt, wcnt

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    put_stone = [list(map(int, input().split())) for _ in range(M)]
    result = occelo(put_stone)
    print(f'#{tc}', *result)



"""
dir = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]

def get_reverse_stone(y, x, bang, color):
    result = []
    dy, dx = dir[bang]
    ny, nx = y, x

    while True: # 무한루프
        ny, nx = ny + dy, nx + dx
        # 범위를 벗어나면
        if nx < 0 or ny < 0 or nx >= N or ny >= N: return []
        # 같은 값을 찾지 못한 경우
        if board[ny][nx] == 0: return []
        # 같은 색을 만나면
        if board[ny][nx] == color:
            result.append((ny, nx))

    return result # 뒤집힌 돌의 좌표


W = 2
B = 1
T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # 보드에 초기돌 4개 세팅
    mid = N // 2
    board[mid - 1][mid - 1] = W # 좌측 위
    board[mid - 1][mid - 0] = B # 우측 위
    board[mid - 0][mid - 1] = B # 좌측 아래
    board[mid - 0][mid - 0] = W # 우측 아래

    for _ in range(M):
        x, y, color = map(int, input().split())
        y, x = y - 1, x - 1

        # 돌을 일단 둔다
        board[y][x] = color

        for bang in range(8):
            # 뒤집을 돌들의 좌표 --> 함수
            target_stones = get_reverse_stone(y,x,bang,color)

            # 뒤집을 돌이 있으면 뒤집기
            if len(target_stones) >= 1:
                for ry, rx in target_stones:
                    if color == B: board[ry][rx] = B
                    else: board[ry][rx] = W

    B_cnt, W_cnt = 0, 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == B: B_cnt +=1
            elif board[r][c] == W: W_cnt += 1

    print(f'#{tc} {B_cnt} {W_cnt}')
"""

"""
# 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
# 그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.
# 돌의 색이 1이면 흑돌, 2이면 백돌이다.
# 만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.
# 돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.


def f(i, j, bw, N):
    # 놓으라고 한 위치 놓기
    board[i][j] = bw
    for di, dj in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
        ni, nj = i + di, j + dj
        tmp = []  # 뒤집을 돌 후보 인덱스 저장

        # 배열을 벗어나지 않는 선에서, 반대색 돌이면
        while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:
            tmp.append((ni, nj))  # 뒤집을 돌을 저장
            ni, nj = ni + di, nj + dj  # 현재 방향으로 계속 이동

        # 같은 색 돌이면
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
            for p, q in tmp:  # 뒤집을 돌들을
                board[p][q] = bw  # 뒤집기


B = 1
W = 2
op = [0, 2, 1]  # 반대색

T = int(input())
for tc in range(1, T + 1):
    # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    N, M = map(int, input().split())
    # 진행 횟수
    play = [list(map(int, input().split())) for _ in range(M)]

    # NxN 보드 0 -> 0 ~ n-1 인덱스 사용
    board = [[0] * N for _ in range(N)]

    # 초기 세팅
    # WB
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    # BW
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    # 돌 놓기
    for col, row, bw in play:  # 좌표 맞추기 해야함 -> 여기서 col row는 1부터
        f(row - 1, col - 1, bw, N)

    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1

    print(f'#{tc} {bcnt} {wcnt}')
"""