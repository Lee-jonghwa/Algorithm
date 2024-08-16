# 만약 민철이가 3번 이하(K = 3)로 버스를 탑승하는 것을 편한다고 느낀다면, 민철이가 이사할 수 있는 지역의 후보는 총 7개 (1, 2, 3, 4, 6, 7, 8번 지역)가 됩니다.

# 총N개의 지역에 대한 버스 노선도의 정보가 주어질 때,민철이가 편하게 출근할 수 있는 지역의 후보지가 몇 군데있는지 출력하는 프로그램을 작성해 주세요.

from collections import deque

def hadanhaeng(S, N, R, K, adjL): #S: 집위치, N: 개수, M 간선개수, R 회사, K 최소 환승, adjLl
    # 준비
    queue = deque()  # 큐 생성
    visited = [0] * (N+1)  # visited 생성
    queue.append(S)  # 시작점 enqueue
    visited[S] = 1   # 시작점 방문표시

    # 처리
    while queue:
        v = queue.popleft()  # dequeue
        # R에 도착했을 때 visited[R] - 1이 K 이하 이면
        if v == R and visited[R] - 1 <= K:
            return 1 # 만족

        for w in adjL[v]:  # 인접한 w에 대해서
            if visited[w] == 0:  # 방문한 적이 없으면
                queue.append(w)  # enqueue
                visited[w] = visited[v] + 1  # 방문표시 -> lev 상승

    # 없으면 0
    return 0


# 지역의 수 N과 버스로 이동 가능한 관계의 수 M
N, M = map(int, input().split())
# M개의 줄에 걸쳐 정수 A, B
arr = [list(map(int, input().split())) for _ in range(M)]
# 직장이 존재하는 지역 R과 출근하기 편하다는기준이 되는 버스 탑승 횟수 K
R, K = map(int, input().split())

# 간선 연결
adjL = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = arr[i][0], arr[i][1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)
cnt = 0
for j in range(1, N+1):
    cnt += hadanhaeng(j, N, R, K, adjL)

print(cnt)