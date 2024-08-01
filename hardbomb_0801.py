def bomb(N, M, K, arr):
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # 2차원 리스트 행 순환
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "@":
                for dy, dx in directions:
                    for k in range(1, K + 1): # 상/하/좌/우
                        ny, nx = i + dy * k, j + dx * k
                        if 0 <= ny < N and 0 <= nx < M:
                            # 폭탄이 터질 수 있는 길이면 터지고
                            if arr[ny][nx] == '_':
                                arr[ny][nx] = '%'
                            # 벽이 있으면 터지지 않음
                            elif arr[ny][nx] == '#':
                                break
                arr[i][j] = "%"

N, M = map(int, input().split())
K = int(input())

arr = [list(input()) for _ in range(N)]
bomb(N, M, K, arr)
for row in arr:
    print(*row, sep="")