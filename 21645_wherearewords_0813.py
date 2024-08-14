T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # 행 검사
    for i in range(N):
        dist = 0 # 연속된 칸의 수
        for j in range(N):
            if puzzle[i][j] == 1: # 흰색을 만나면
                dist += 1
            if puzzle[i][j] == 0 or j == N - 1: # 검은색이거나 행 끝에 도달
                if dist == K:
                    cnt += 1
                dist = 0

    # 열 검사
    for j in range(N):
        for i in range(N):
            if puzzle[i][j] == 1: # 흰색을 만나면
                dist += 1
            if puzzle[i][j] == 0 or i == N - 1: # 열 끝에 도달
                if dist ==K:
                    cnt += 1
                dist = 0

    print(f'#{tc} {cnt}')






"""
def check_line(line, K):
    cnt = 0
    ones = 0

    for cell in line:
        if cell == 1:  # cell 이 흰색일 경우
            ones += 1
        else:  # cell이 검은색인 경우
            if ones == K: # 1의 연속된 갯수가 K와 같다면
                cnt += 1
            ones = 0 # 연속된 1의 갯수 초기화

    # 라인 끝에서 확인
    if ones == K:
        cnt += 1

    return cnt

def cnt_spaces(puzzle, N, K):
    cnt = 0

    # 가로 방향 확인
    for row in puzzle:
        cnt += check_line(row, K)

    # 세로 방향 확인
    # for col in range(N):
    #     column = []
    #     for row in range(N):
    #         column.append(puzzle[row][col])
    #     cnt += check_line(column, K)
    for col in zip(*puzzle):
        cnt += check_line(col, K)

    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = cnt_spaces(puzzle, N, K)
    print(f'#{tc} {result}')
"""


"""
def find_words(N, K, arr):
    cnt = 0

    # 가로 방향 체크
    for y in range(N):
        length = 0
        for x in range(N):
            if arr[y][x] == 1:
                length += 1
            else:
                if length == K:  # K가 5 미만일 때
                    cnt += 1
                length = 0
        if length == K:  # K가 5일 때
            cnt += 1

    # 세로 방향 체크
    for x in range(N):
        length = 0
        for y in range(N):
            if arr[y][x] == 1:
                length += 1
            else:
                if length == K:
                    cnt += 1
                length = 0
        if length == K:
            cnt += 1

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = find_words(N, K, arr)
    print(f"#{tc} {result}")
"""