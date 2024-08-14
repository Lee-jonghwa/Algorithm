n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]

def dfs(now): # 출력할 now를 매개변수로
    print(now, end=" ")
    for i in range(n):
        if MAP[now][i] == 1:  # 현재 위치에서 i로 갈 수 있는 길이 있으면
            dfs(i)

dfs(0)


"""
def dfs(s, N): # s: 시작 정점, N: 노드 개수
    global path
    # 준비
    visited = [0] * N # visited 생성
    stack = [] # 스택생성
    visited[s] = 1
    path.append(s) # 경로 확인
    v = s
    # 처리
    while True: # 무한루프
        for w in range(N): # v에 인접한 요소 찾기
            if visited[w] == 0 and arr[v][w] == 1: # 방문한 적 없고 값이 있는
                stack.append(v) # 현재 정점 push
                v = w # 이동

                path.append(v)  # 현재 정점 기록
                visited[w] = 1
                break               # for 문 돌고 다시 탐색
        else:
            if stack:               # 스택에 남은 게 있다면
                v = stack.pop()     # 다시 되돌아감
            else:
                break


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
path = []

dfs(0, N)
print(*path)

"""