"""
# BFS
def BFS(G, v):                          # G: 그래프, v: 탐색시작 지점
    visited = [0]*(n+1)                 # n: 정점의 갯수, visited의 인덱스를 맞춰주기 위함
    queue = []                          # 큐 생성
    queue.append(v)                     # 큐에 시작점 v 삽입(enqueue)
    while queue:                        # 큐가 비어있지 않은 경우
        t = queue.pop()                 # 큐의 첫 번째 원소 반환(방문/처리할 노드-> dequeue)
        if not visited[t]:              # 방문되지 않은 곳이라면
            visited[t] = True           # 방문 표시
            for i in G[t]:              # t와 연결된 i들에 대해
                if not visited[i]:      # 방문되지 않은 곳이라면
                    queue.append(i)     # 큐에넣기
"""


"""
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, v): # 시작점 s, 정점수(마지막정점) v --> 마지막 정점이 꼭 goal은 아님
    # 준비
    visited = [0] * (v + 1)         # visited 생성
    queue = []                      # queue 생성
    queue.append(s)                 # 시작점 enqueue
    visited[s] = 1                  # 시작점 방문(enqueue) 표시
    # 탐색
    while queue:                    # 큐가 비어있지 않으면, 탐색할 정점이 남아 있으면
        t = queue.pop(0)            # deque
        print(t)                    # 처리
        for w in adjL[t]:           # t에 인접한 요소들
            if visited[w] == 0:     # enqueue 된 적이 없으면
                queue.append(w)     # enqueue 하고
                visited[w] = visited[t] + 1      # enqueue 표시
    print(visited)



v, E = map(int, input().split())  # v는 마지막 정점 번호
arr = list(map(int, input().split())) # 간선 이어지는 리스트
adjL = [[] for _ in range(v+1)]  # 인접 정점 리스트 # adjL[0] --> 0번 정점에 인접인 정점 ==> 1부터 시작되므로 v+1
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)  # 돌아오는 경우 추가(방향이 없는 경우) but 입력이 출발 도착일지 확인할 필요는 있음

bfs(1, v)
"""



"""
# 5105 문제 실습

# 인접 조건: 벽이 아닌, 사방향, 방문한 적 없는

# dequeue한 다음

# ti, tj -> if maze[ti][tj] == 3:

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


def bfs(sti, stj, N):
    # 준비
    visited = [[0]*N for _ in range(N)]
    queue = []          # queue 생성
    queue.append([sti,stj]) # 시작점 enqueue
    visited[sti][stj] = 1   # 시작점 enqueue 표시

    # 탐색
    while queue:
        ti, tj = queue.pop(0)  # dequeue
        if maze[ti][tj] == 3:  # 도착 시 - visit(t)
            # 사이에 있는 빈칸의 갯수 -> visited - 1
            return visited[ti][tj] - 1 - 1  # 출발지 위치는 항상 1, 경로의 빈칸 수
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 인접이고, 벽이 아니면, 미로를 벗어나지 않고
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                queue.append([wi,wj])               #enqueue
                visited[wi][wj] = visited[ti][tj] + 1 # enqueue 표시
    return 0 # 도달 못하는 경우


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')
"""

"""
BFS
1. Queue를 사용하여 구현 -- deque 모듈 사용
2. 거리가 같은 노드를 탐색한 후 다음 깊이의 노드로 이동 ==> lev 순서로 탐색
3. 최단 경로 문제 해결하는데 자주 사용 --> 우선순위큐(heap) ==> 다익스트라

node 와 node j 가 연결되있으면 1, 아니면 0

"""

"""
def bfs(s, v): # 시작점 s, 정점수(마지막정점) v --> 마지막 정점이 꼭 goal은 아님
    # 준비
    visited = [0] * (v + 1)         # visited 생성
    queue = []                      # queue 생성
    queue.append(s)                 # 시작점 enqueue
    visited[s] = 1                  # 시작점 방문(enqueue) 표시
    # 탐색
    while queue:                    # 큐가 비어있지 않으면, 탐색할 정점이 남아 있으면
        t = queue.pop(0)            # deque
        print(t)                    # 처리
        for w in adjL[t]:           # t에 인접한 요소들
            if visited[w] == 0:     # enqueue 된 적이 없으면
                queue.append(w)     # enqueue 하고
                visited[w] = 1      # enqueue 표시
                #visited[w] = visited[t] + 1  # lev 나눌 때 사용 1 - 2 - 3



v, E = map(int, input().split())  # v는 마지막 정점 번호
arr = list(map(int, input().split())) # 간선 이어지는 리스트
adjL = [[] for _ in range(v+1)]  # 인접 정점 리스트 # adjL[0] --> 0번 정점에 인접인 정점 ==> 1부터 시작되므로 v+1
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)  # 돌아오는 경우 추가(방향이 없는 경우) but 입력이 출발 도착일지 확인할 필요는 있음

bfs(1, v)

"""


'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

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