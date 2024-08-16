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