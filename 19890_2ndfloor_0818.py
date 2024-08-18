def dfs(s, n):  # n -> 노드 수
    global path
    # 준비
    visited = [0] * n # visited 배열 생성
    stack = []  # 스택 생성
    visited[s] = 1  # 시작 정점 방문 표시
    path.append(s)  # 시작 정점 경로 추가
    v = s   # 지점 설정

    # 처리
    while True: # 무한루프
        for w in range(n): # 인접하고 있는 요소 중
            if visited[w] == 0 and arr[v][w] == 1:  # 방문 안 한 요소에 대해, 배열에 값이 있으면
                stack.append(v)  # 현재 정점 push
                visited[w] = visited[v] + 1  # 방문 표시, lev표시
                v = w   # w로 지점 옮김
                path.append(v)  # 현재 정점 기록
                if visited[w] == 3:
                    print(*path)
                break  # 중단

        else:  # 남은 인점 정점이 없는 경우
            if stack:  # 스택에 남은 게 있으면음
                v = stack.pop()  # 이전 갈림길 스택에서 꺼냄
                path.pop() # path 지워주기
            else:  # 되돌아갈 곳이 없으면
                break  # 탐색 종료


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
path = [] # path 생성

dfs(0, n)

