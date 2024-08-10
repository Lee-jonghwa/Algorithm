def DFS(s, n):                          # s: 시작정점 n: 정점개수(1번부터인 정점의 마지막)
    visited = [0]*(n+1)                 # 방문한 정점을 표시
    stack = []                          # 스택 생성
    print(s)
    visited[s] = 1                      # 시작 정점 방문 표시
    v = s                               # 지점 설정
    while True:
        for w in adjL[v]:               # v에 인접하고 방문 안 한 w 가 있으면
            if visited[w] == 0:
                stack.append(v)         # 현재 정점 push
                v = w                   # w에 방문
                print(v)
                visited[w] = 1          # 방문 표시
                break                   # for w... v부터 다시 탐색
        else:                           # 남은 인접 정점이 없어서 break 없는 경우 => 요소를 다 돌고 나서
            if stack:                   # 스택에 남은 게 있으면
                v = stack.pop()         # 이전 갈림길을 스택에서 꺼내서
            else:                       # 되돌아갈 곳이 없으면(남은 갈림길이 없으면)
                break                   # while True... 탐색 종료

T = int(input())
for tc in range(1, T+1):
    v, E = map(int, input().split())    # v: 현재정점 E: 간선 수 (연결된 길)
    adjL = [[] for _ in range(v+1)]     # 인접 정점 리스트를 구하기 위함
    arr = list(map(int, input().split()))
    for i in range(E):                  # 간선에서 두 개씩 가져오는 작업
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)             # adjL이 비어있는 상테에서 1번행의 2번 열에 append --> 가는 방향
        adjL[v2].append(v1)             # 오는 방향 추가
        # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]] 각 요소 index가 출발점
    DFS(1, 7)