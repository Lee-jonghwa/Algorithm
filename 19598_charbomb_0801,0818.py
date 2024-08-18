
# 차르봄바는 P 크기만큼으로
# 가로, 세로 방향
# N x N 크기의 마을의
# 가장 많은 바이러스를 제거했을 때 제거된 바이러스의 수를 구하여라

def charbomb():
    max_v = 0

    for y in range(N):
        for x in range(N):
            # 이번 합계값 초기화, 터진자리 포함
            sum_v = town[y][x]
            for dy, dx in directions:
                for k in range(1, P+1): # 제자리 제외, P까지 가야함
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < N and 0 <= nx < N: # 배열을 벗어나지 않을 때
                        sum_v += town[ny][nx]
            if max_v < sum_v:
                max_v = sum_v

    return max_v

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    town = [list(map(int, input().split())) for _ in range(N)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    result = charbomb()
    print(f'#{tc} {result}')


"""
def bomb(N, P, arr):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    max_sum = float('-inf')

    for i in range(N):
        for j in range(N):
            cnt = arr[i][j]  # 현재 위치 위치값으로 초기화
            for dir in range(4):  # 상하좌우 순회 후
                for k in range(1, P + 1):
                    ny, nx = i + dy[dir] * k, j + dx[dir] * k
                    if 0 <= ny < N and 0 <= nx < N:
                        cnt += arr[ny][nx]
            max_sum = max(cnt, max_sum)
    return max_sum


T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = bomb(N, P, arr)
    print(f'#{tc} {result}')

"""

"""

T = int(input())

directions = [(0, 1), (-1,0), (0, -1), (1, 0)] # 우 상 좌 하

for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    max_v = 0 # 최종 바이러스 초기화
    for i in range(N):
        for j in range(N): # 모든 행렬 순회
            sum_v = 0 # 한 회마다 바이러스
            sum_v += arr[i][j] # 터진 자리 더하기
            for dy, dx in directions:
                for p in range(1, P+1): # 파워 반영
                    ny, nx = i + dy * p, j + dx * p
                    if 0 <= ny < N and 0 <= nx < N:
                        sum_v += arr[ny][nx]
            if max_v < sum_v:
                max_v = sum_v
    print(f'#{tc} {max_v}')

"""