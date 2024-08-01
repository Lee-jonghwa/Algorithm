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