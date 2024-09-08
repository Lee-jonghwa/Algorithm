import sys
sys.stdin = open('2819_input.txt','r')

# 4×4 크기의 격자판이 있다. 격자판의 각 격자칸에는 0부터 9

# 동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동

# 한 번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 0102001과 같은 수를 만들 수도 있다.

# 서 로 다른 일곱 자리 수들의 개수


directions = [(0,1),(0,-1),(-1,0),(1,0)]

def dfs(lev, y, x):
    global path

    if lev == 7:
        result.add(path)
        return

    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if ny >= 4 or ny < 0 or nx >= 4 or nx <0: continue # 배열을 넘지 않는 선에서
        path += arr[ny][nx]
        dfs(lev + 1, ny, nx)
        path = path[:-1]


T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]

    result = set()

    # 시작점을 모든 칸으로
    # visited 필요 없음

    for y in range(4):
        for x in range(4):
            path = ""
            dfs(0, y, x)

    print(f'#{tc} {len(result)}')



"""
# DFS

# 거쳤던 격자칸을 다시 거쳐도 됨 -> 무조건 7칸 확인 가능
# 서로 다른 일곱 자리 수 -> 중복 제거(set)


# 문자열의 거리가 7이면 종료
directions = [(0,1),(1,0),(0,-1),(-1,0)]

def dfs(y, x, path):
    if len(path) == 7:
        result.add(path)  # 현재 값의 경로를 결과 set에 저장
        return

    for dy, dx in directions:
        ny = y + dy
        nx = x + dx
        # 배열을 벗어나지 않는 선에서
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny,nx,path + arr[ny][nx]) #문자열 누적

T = int(input())
for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    # 중복을 제거
    result = set()

    # 모든 지점을 확인
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])  # 6칸 이동 후 필요한 정보 -> 좌표, 누적 문자열

    print(f'#{tc} {len(result)}')
"""