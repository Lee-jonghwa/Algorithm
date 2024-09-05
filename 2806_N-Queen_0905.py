def check(row):
    for col in range(row): # 모든 열에 대한 내용 중에서
        if visited[row] == visited[col]:
            # 내가 두려는 위치가 이미 퀸이 있는 같은 열이라면
            return False

        # 열과 행의 차이가 같다 == 현재 col에 대해 좌우 대각선 상태이다
        if abs(visited[row] - visited[col]) == abs(row - col):
            return False

    # 둘 다 아니라면
    return True

def dfs(row):
    global cnt

    # 모든 열을 순회하면
    if row == N:
        cnt += 1
        return

    #
    for col in range(N):
        visited[row] = col
        # 각 행에 queen을 두는 위치를 col
        if not check(row):
            continue

        dfs(row+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    visited = [0]*N
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')


# N*N 보드에 N개의 퀸을 서로 다른 두 퀸이 공격하지
# 못하게 놓는 경우의 수는 몇가지가 있을까?
# 백트래킹
# 공격 하는 경우 백트래킹
# 위에서 아래만 가능
# 서로 다른 두 퀸이 공격하지 못하게 놓는 경우의 수는 몇가지가 있을까?
"""
def is_safe(row, col, board):
    # 같은 열에 있는지 확인
    for i in range(row):
        if board[i] == col:
            return False
        # 대각선에 있는지 확인
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def n_queens(row, board, N):
    # 마지막 행 까지 탐색이 끝나면
    if row == N:
        return 1
    count = 0
    for col in range(N):
        if is_safe(row, col, board, N):
            board[row] = col
            count += n_queens(row + 1, board)
    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 모든 행의 경우 세팅
    board = [-1] * N
    result = n_queens(0, board, N)
    print(f'#{tc} {result}')
"""

"""
from collections import deque

# 오른쪽 또는 아래
atk_directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
set_directions = [(0,1), (1,0)]


def n_queen(arr,start):
    global cnt

    # bfs
    q = deque([start]) # 경로 저장
    visited = [[0] * N for _ in range(N)] # visited 배열 생성

    while q:
        now = q.popleft()
        # 종료조건 마지막 줄에 눴으면
        if now[0] == N-1:
            cnt += 1
            return

        # 못 가는 자리 체크(공격 범위 체크)
        for ady, adx in atk_directions:
            for k in range(N):
                ay, ax = now[0] + ady * k, now[1] + adx * k
                if 0 <= ay < N and 0 <= ax < N:
                    visited[ay][ax] = 1 # 다른 걸로 둬서 애초에 못가게

        for dy, dx in set_directions:
            ny, nx = now[0], now[1]
            #배열을 벗어나지 않고, 이전 것의 8방향이 아닐 때
            if 0 <= ny < N and 0 <= nx <N and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append(now)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    cnt = 0
    n_queen(arr,(0,0))

    print(f'#{tc} {cnt}')
"""