directions = [(1,0),(0,1),(-1,0),(0,-1)]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]

    visited = [0] * (N*N+1)

    # 전체를 순회하며
    # 상하좌우에 나보다 1이 크면 visited 체크
    for i in range(N):
        for j in range(N):
            for dy, dx in directions:
                ny = i + dy
                nx = j + dx
                if 0<=ny<N and 0<=nx<N:
                    # 옆이 1보다 크다면, 나는 움직일 수 있음을 표시
                    if arr[ny][nx] == arr[i][j] + 1:
                        visited[arr[i][j]] = 1
                        # 체크된 순간 다른방을 볼 필요가 없음
                        break

    # cnt: 하나씩 체크/ max_cnt: 결과값 / # 시작 위치
    cnt = 1
    max_cnt = start = 0

    for i in range(N*N -1, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1 # 배열 안에서 나오도록
            cnt = 1
            # cnt 초기화

    print(f'#{tc} {start} {max_cnt}')

# def DFS(s, n):                          # s: 시작정점 n: 정점개수(1번부터인 정점의 마지막)
#     visited = [0]*(n+1)                 # 방문한 정점을 표시
#     stack = []                          # 스택 생성
#     print(s)
#     visited[s] = 1                      # 시작 정점 방문 표시
#     v = s                               # 지점 설정
#     while True:
#         for w in adjL[v]:               # v에 인접하고 방문 안 한 w 가 있으면
#             if visited[w] == 0:
#                 stack.append(v)         # 현재 정점 push
#                 v = w                   # w에 방문
#                 print(v)
#                 visited[w] = 1          # 방문 표시
#                 break                   # for w... v부터 다시 탐색
#         else:                           # 남은 인접 정점이 없어서 break 없는 경우 => 요소를 다 돌고 나서
#             if stack:                   # 스택에 남은 게 있으면
#                 v = stack.pop()         # 이전 갈림길을 스택에서 꺼내서
#             else:                       # 되돌아갈 곳이 없으면(남은 갈림길이 없으면)
#                 break                   # while True... 탐색 종료
#
# T = int(input())
# for tc in range(1, T+1):
#     v, E = map(int, input().split())    # v: 현재정점 E: 간선 수 (연결된 길)
#     adjL = [[] for _ in range(v+1)]     # 인접 정점 리스트를 구하기 위함
#     arr = list(map(int, input().split()))
#     for i in range(E):                  # 간선에서 두 개씩 가져오는 작업
#         v1, v2 = arr[i*2], arr[i*2+1]
#         adjL[v1].append(v2)             # adjL이 비어있는 상테에서 1번행의 2번 열에 append --> 가는 방향
#         adjL[v2].append(v1)             # 오는 방향 추가
#         # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]] 각 요소 index가 출발점
#     DFS(1, 7)


import math
def repeater(N,lction):
    repeater_lction = None
    house_lction = []
    for y in range(N):
        for x in range(N):
            if lction[y][x] == 2 :
                repeater_lction = (y,x)
            elif lction[y][x] == 1:
                house_lction.append((y,x))

    max_distance_sq = 0

    ry, rx = repeater_lction
    for hy, hx in house_lction:
        distance_sq = (hy - ry) ** 2 + (hx - rx) ** 2
        max_distance_sq = max(max_distance_sq, distance_sq)


    min_r = math.ceil(math.sqrt(max_distance_sq))
    return min_r


T = int(input())
for tc in range(1,T+1):
    N = int(input())+1
    lction = [list(map(int, input().split())) for _ in range(N)]
    result = repeater(N,lction)
    print(f'#{tc} {result}')