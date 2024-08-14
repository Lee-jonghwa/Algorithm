def bfs(S, G, V):
    # 준비
    queue = []  # queue 생성
    visited = [0] * (V + 1) # visited 배열 생성(인덱스 맞춤 위해 +1)
    queue.append(S) # 시작점 enqueue
    visited[S] = 1  # 시작점 방문표시
    # 처리
    while queue:    # queue가 살아있는동안
        t = queue.pop(0)# deque
        if t == G:# G에 도달했으면
            return visited[G] - 1 # G까지의 visited - 1(간선 개수이므로)
        for w in adjL[t]:# 인접한 요소에 대해
            if visited[w] == 0: # 방문하지 않았으면
                queue.append(w)# enqueue
                visited[w] = visited[t] + 1 # 방문표시
    return 0 # 간선의 개수를 구하므로 lev가 중요

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V: 노드 개수(최대 노드) E: 간선 개수
    arr = [list(map(int, input().split())) for _ in range(E)]  # 간선
    adjL = [[] for _ in range(V+1)] # 인덱스 맞춰주기 위해 +1
    # 인접 리스트 정리
    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    S, G = map(int, input().split())  # S: 출발 노드 G: 도착 노드
    result = bfs(S, G, V)
    print(f'#{tc} {result}')


