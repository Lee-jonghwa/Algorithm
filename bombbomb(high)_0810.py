N, M = map(int, input().split()) # N: 세로길이, M: 가로 길이
K = int(input()) # 화력
arr = [list(input()) for _ in range(N)] # 배열

directions = [(-1,0),(0,-1),(1,0),(0,1)] # 상하좌우

for y in range(N):
    for x in range(M):
        if arr[y][x] == '@': # 폭탄이 있는 경우에 대해서
            arr[y][x] = '%' # 터진 자리도 폭파기록
            for dy, dx in directions:  # 모든 방향에 대해
                for k in range(1, K+1): # 폭탄 화력 -> 1 ~ K까지
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '_':
                        # 배열을 넘지 않은 선에서 통로에 해당하는 부분만
                        arr[ny][nx] = '%'
                    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == '#':
                        # 벽이 있으면
                        break # 넘어감


for i in range(N):
    print(*arr[i], sep="")

# 범위를 틀려서 틀림,,, 범위에 대한 정보 잘 읽기!