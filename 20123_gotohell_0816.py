
from collections import deque

def bfs(N, adjL):
    # 준비
    queue = deque()  # 큐 생성
    visited = [0] * (N + 1)  # visited 생성
    queue.append(1)  # 시작점 enqueue
    visited[1] = 1  # 시작점 표시

    # 처리
    while queue:
        v = queue.popleft()  # dequeue
        # 최소 환승 횟수를 출력
        if v == N: # 도착했을 때
            # 0아닌 visited 중에서
            return visited[N] - 1 # 도착지점 N에 방문했을 때 출발점 뺀 값
        for w in adjL[v]: # 인접한 정류장들 중에서
            if visited[w] == 0 and w != T: # 방문 안 하고, T가 아닌 곳에
                queue.append(w)
                visited[w] = visited[v] + 1
    return -1


N, M = map(int, input().split()) # 지역의 수, 도착점 N, 관계의 수 M
arr = [list(map(int, input().split())) for _ in range(M)]
adjL = [[] for _ in range(N+1)]
T = int(input()) # 화재 발생 지역

for i in range(M):
    v1, v2 = arr[i][0], arr[i][1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)

result = bfs(N, adjL)
print(result)