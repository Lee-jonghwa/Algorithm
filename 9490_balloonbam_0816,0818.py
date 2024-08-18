
# 풍선이 M개씩 N개의
# 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임이 있다.
# 날릴 수 있는 꽃가루의 합 중 최대값을 출력하는 프로그램

directions = [(1,0),(-1,0),(0,1),(0,-1)]


def poongs():
    max_v = 0
    for y in range(N):
        for x in range(M):
            start = arr[y][x]  # 각 위치별 최대 합산
            sum_v = start
            for dy, dx in directions:
                for k in range(1, start + 1): # 꽃가루 나온것만큼
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < N and 0 <= nx < M: # 배열을 벗어나지 않는 선에서
                        sum_v += arr[ny][nx]
            if max_v < sum_v:
                max_v = sum_v
    return max_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = poongs()
    print(f'#{tc} {result}')


"""
# 한 행 풍선 개수(열 개수): M
# 행 개수: N
# 칸마다의 꽃가루: A
# 첫 자리를 보고 -> 그만큼 상하좌우 추가

directions = [(-1,0),(0,-1),(1,0),(0,1)]

### 값을 곱해줘서 퍼지는 방식 풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 행, 열 크기 --> 순서 잘 보기
    A = [list(map(int, input().split())) for _ in range(N)] # 풍선별 꽃가루

    max_v = 0   # 꽃가루 최대 합계
    for y in range(N):  # N 행
        for x in range(M):  # M 열
            sum_v = A[y][x]  # 터뜨리는 자리 포함
            for dy, dx in directions:
                # 나온 갯수만큼 퍼지기, 한 칸 옆부터 값만큼
                for k in range(1, A[y][x] + 1):
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < N and 0 <= nx < M:
                        sum_v += A[ny][nx]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')


"""

""" 누적 풀이 연습해보기
### 값을 누적으로 더하는 풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for y in range(N):  # N 행
        for x in range(M):  # M 열
            sum_v = A[y][x]  # 터뜨리는 자리 포함
            # 주변 풍선 꽃가루 수
            for dy, dx in directions:
                # 주변 방향으로 추가로 터지는 풍선과의 거리
                for k in range(A[y][x]): # 나온 갯수만큼 방향 전진
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        sum_v += A[ny][nx]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')
"""