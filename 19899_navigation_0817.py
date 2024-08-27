def dfs(A, B, N): # s: 시작 정점, N: 노드 개수
    # 준비
    visited = [0] * (N + 1) # visited 생성
    stack = [] # 스택생성
    visited[A] = 1
    stack.append(A) # 경로 확인
    # 처리
    while True: # 무한루프
        v = stack.pop()

        if v == B:
            return visited[v] - 1  # 방문깊이 -1

        for w in arr[v]: # v에 인접한 요소 찾기
            if visited[w] == 0: # 방문한 적 없고 값이 있는
                stack.append(w) # 현재 정점 push
                visited[w] = visited[v] + 1

A, B = map(int, input().split())
arr = [[],[3, 5, 6],[1, 4],[5],[1],[1],[]]
N = 6
stack = [A]  # 첫 요소 삽입
visited = [0] * (7)
visited[A] = 1  # 방문표시
result = dfs(A, B, N)
print(result)








"""
# 노드 번호 2개(A, B)를 입력받아주세요.
#
# A 에서 B 까지 최소 몇 회만에 도착할 수 있는지 출력 해 주세요
# 갈수 없다면 0
def dfs(A, B, N):
    # 준비
    stack = []  # 스택생성
    visited = [0] * (N + 1) # visited 생성
    visited[A] = 1  # 첫자리 방문표시
    stack.append(A)  # path 추가

    # 처리
    while True:# 무한루프
        v = stack.pop()

        # 목적지에 도달하면
        if v == B:
            return visited[v] - 1  # 방문깊이 -1

        for w in adjL[v]:# 인접해 있는 원소에 대해서
            if visited[w] == 0:# 방문 안 했으면
                stack.append(w)# 현재 위치 push
                visited[w] = visited[v] + 1  # 방문표시, lev반영
        return 0



adjL = [[],[3,5,6],[1,4],[5],[1],[1],[]]
N = 6
A, B = map(int,input().split())
result = dfs(A, B, N)
print(result)

"""