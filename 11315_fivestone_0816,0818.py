
# 오른쪽, 오른쪽아래, 아래, 왼쪽아래
directions = [(0,1),(1,1),(1,0),(1,-1)]

def omok(game):
    for y in range(N):
        for x in range(N):
            if game[y][x] == 'o':
                for dy, dx in directions:
                    cnt = 1  # 오목 세기
                    for k in range(1, 5):
                        ny, nx = y + dy * k, x + dx * k
                        if 0 <= ny < N and 0 <= nx < N and game[ny][nx] == 'o':
                            cnt += 1
                            if cnt == 5:
                                return "YES"
                        else:
                            break # 안 나오면 더 갈 필요가 없음
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    game = [input() for _ in range(N)]
    result = omok(game)
    print(f'#{tc} {result}')




"""
def omok(y, x):
    dy = [1, 0, 1, -1]  # 아래, 우측, 우측 하단, 우측 상단
    dx = [0, 1, 1, 1]

    for d in range(4):
        cnt = 1

        for p in range(1, 5): # 4칸 더 찾기
            ny = y + dy[d] * p
            nx = x + dx[d] * p
            if not (0 <= ny < n and 0 <= nx < n): break # 배열 벗어나면 중지
            if arr[ny][nx] == 'o': cnt += 1 # 방향 탐색에 돌 있으면 카운팅

            if cnt == 5:  # 오목이면
                return True
    return False

def game_start():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                if omok(i, j):
                    return "YES"
    return "NO"

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(n)]
    result = game_start()
    print(f'#{tc} {result}')
"""

"""
# N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다

# 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.

# 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”

di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]
def f(N):
    for i in range(N):
        for j in range(N):
            # 네 방향으로
            for k in range(4):
                cnt = 0 # 돌의 개수
                ni, nj = i, j # 돌이 있는지 확인
                while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 'o':
                    cnt += 1

                    # 다섯 개면
                    if cnt == 5:
                        return "YES"

                    # 다섯 개가 안 되면
                    ni += di[k]
                    nj += dj[k]

    # 모든 자리에서 모든 방향에 대해 실패하면
    return "NO"


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 오목판 크기
    arr = [input() for _ in range(N)]  # 오목판
    ans = f(N)
    print(f'#{tc} {ans}')
"""

"""
def fivestone(N, arr):
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o':  # 돌이 있는 위치에서만 시작
                for dy, dx in [(0, 1), (1, 0), (1, 1), (1, -1)]: # 찍는 점이 무조건 시작점이라고 가정하면
                    cnt = 0
                    for k in range(5):
                        ny, nx = y + dy * k, x + dx * k # 한 방향에 해서 5번 전진, 제자리 포함되도 상관 없음
                        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o': # 해당 방향이 o 면
                            cnt += 1
                        else:
                            break  # 5개 연속되지 않으면 break
                    if cnt == 5:  # 5개 연속된 경우
                        return "YES"
    return "NO"  # 5개 연속된 돌이 없는 경우


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [input().strip() for _ in range(N)]  # 입력을 리스트로 받아 처리
    result = fivestone(N, arr)
    print(f'#{tc} {result}')


# 배열로 접근해보기
"""
"""
def fivestone(N, arr):
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 'o': # o인 곳을 하나 찍어서
                slash1 = 0  # 정방향 대각선 / 시작점이 이미 o 기 때문에 1로 시작
                slash2 = 0  # 역방향 대각선
                v = 0       # 세로
                h = 0       # 가로
                for dy, dx in [(-1, -1), (1, 1), (1,-1), (-1,1),(-1, 0), (1, 0),(0, -1), (0, 1)]:
                    for k in range(5): # 5칸 이상이기만 하면 됨 # 자리 포함 값
                        ny, nx = y + dy * k, x + dx * k
                        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o': # 배열을 넘지 않는 선에서 o 추가
                            if (dy, dx) == (-1, -1) or (dy, dx) == (1, 1): # 정방향으로 펴지면
                                slash1 += 1
                            elif (dy, dx) == (-1, 1) or (dy, dx) == (1, -1): # 역방향으로 펴지면
                                slash2 += 1
                            elif (dy, dx) == (-1, 0) or (dy, dx) == (1, 0): # 세로로 퍼지면
                                v += 1
                            else: # 가로로 펴지면
                                h += 1
                if slash1 >= 5 or slash2 >= 5 or v >= 5 or h >= 5:  # 어느 방향이라도 5개 이상이 있으면
                    cnt += 1
    if cnt: # 하나라도 있으면
        return "YES"
    else:
        return "NO"



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = fivestone(N, arr)
    print(f'#{tc} {result}')
"""