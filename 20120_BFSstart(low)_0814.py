from collections import deque

n = int(input())
MAP = []
for _ in range(n):
    MAP.append(list(map(int, input().split())))

def bfs(node): # node : 시작 노드
    q = deque([node]) # 시작 노드 queue에 추가
    visited = [0] * n # visited 배열 생성
    visited[node] = 1 # 시작 노드 방문 표시
    while q: # q가 빌 때까지.
        now = q.popleft() # 현재 위치
        print(now, end=" ")
        for i in range(n):
            # 이미 방문했거나, 연결되어 있지 않은 노드(인접행렬이 0이면)
            if MAP[now][i] == 0 or visited[i] == 1:
                continue # 넘어감
            visited[i] = 1
            q.append(i)

bfs(0)

"""
def bfs(s, N): # s: 시작점, N: 노드의 갯수
    global path
    # 준비
    queue = []                          # queue 생성
    visited = [0]*N # visited 생성
    queue.append(s)              # 시작점 enqueue
    visited[s] = 1                 # 시작점 방문 표시
    # 처리
    while queue: # queue가 존재하는 동안
        t = queue.pop(0) # deque
        path.append(t)
        for w in range(N): # 인접 행에 있는 요소들에 대해
            if visited[w] == 0 and arr[t][w] == 1:  # 값이 있고, 방문한 적 없으면
                queue.append(w)
                visited[w] = 1
            else:
                continue

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
path = []

bfs(0, N)
print(*path)
"""