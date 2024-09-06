import sys
sys.stdin = open('2819_input.txt','r')


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