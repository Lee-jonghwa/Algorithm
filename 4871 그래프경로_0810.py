def dfs(start,end):
    stack =[] #빈스텍
    visited=[0]*(V+1)
    stack.append(start) #시작점 스택에 넣기

    while stack:
        now=stack.pop() #스택의 마지막 노드를 제거하고 반환
        visited[now]=1 #현재 노드를 방문했다고 기록
        for next in range(1,V+1):
            #node는 인접행렬
            #now현재 next다음
            if node[now][next] and not visited[next]: #간선으로 연결되어있고, 방문하지 않았다면
                stack.append(next) #스택에 추가
    if visited[end]: # 끝점에 방문했다면
        return 1
    else: return 0

T=int(input())
for tc in range(1,T+1):
    V,E=map(int, input().split())
    node=[[0 for _ in range(V+1)] for _ in range(V+1)] #인접행렬 초기화
    for _ in range(E):
        start, end= map(int, input().split())
        node[start][end]=1 #인접행렬에 1 기록 -> 간선으로 연결되어 있음
    S,G=map(int,input().split())
    print(f'#{tc} {dfs(S,G)}')



'''
def grline(S, V, G): # S: 시작 정점 V: 정점(노드) 개수 # G: 도착점
    visited = [0] * (V + 1) #정점 개수에 맞게 인덱스 맞추기 위함
    stack = [S]
    while stack: # 될 때까지 순회
        v = stack.pop() # 스택 가장 위에 있는 게 내 위치
        # 층이 나누어져 있어도 현재 내가 있눈 곳을 다 쓰면 이전으로 감

        if v == G: # 정점에 도달하면
            return 1

        if not visited[v]: # 방문한 적 없으면
            visited[v] = 1 # 방문 첵
            for w in adjL[v]: # 인접 정점 리스트 중 방문 안 한 w에 대해
                stack.append(w) # 스택 기록
    return 0 # 다 못 찾으면 실패

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V는 노드갯수, E는 간선 수
    adjL = [[] for i in range(V+1)]
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split()) # S는 시작점, G는 도착점
    for i in range(E): # 간선에서 요소 두개 get
        v1, v2 = arr[i][0], arr[i][1] # 하나와 그 다음 것
        adjL[v1].append(v2) # adjL이 비어있는 상태에서 두 개 연결 (한 방향이므로 하나만 연결)
    print(f'#{tc} {grline(S, V, G)}')
'''