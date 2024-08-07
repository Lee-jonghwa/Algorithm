# memo를 위한 배열을 할당, 0으로 초기화
# memo[0]은 0으로 memo[1]은 1로 초기화
# memo[0] == fibo(0)
# memo 값이 곧 함수값

# def fibo1(n):
#     global memo
#     if n >= 2 and memo[n] == 0: # fibo1(n)이 계산된 적이 없는 상태
#         memo[n] = fibo1(n-1) + fibo1(n-2)
#     return memo[n]
#
# n = 7
# memo = [0] * (n+1)
# memo[0] = 0
# memo[1] = 1
# fibo1(n)
# print(fibo1(n))
# print(memo)


# def fibo(n):
#     if n >= 2: # fibo1(n)이 계산된 적이 없는 상태
#         return fibo(n-1) + fibo(n-2)
#     else:
#         return n
#
# fibo(n)
# print(fibo(n)) # 시간복잡도 2**n -> 같은 값이더라도 훨씬 빠름


## 피보나치 처럼 알려진 것에서는 문제가 되지 않겠지만, 그렇지 않다면 수식에 맞게 해야할 필요 있음


### DFS 알고리즘

'''
# visited, stack 초기화
visited = []
stack = []

DFS(v):
    시작점 v 방문
    visited[v] <- true;
    while {
        if v의 인접 정점 중 방문 안 한 정점 w가 있으면
            push(v);
            v <- w; (w 방문)
            visited[w] <- true;
        else
            if 스택이 비어있지 않으면
                v <- pop(stack);
            else
                break
    }
end DFS
'''

'''
### 연습문제
# 12 13 24 25 46 56 67 37 -> 간선(요소간 연결된 길
# 1 2 4 6 5 6 7 3 7 6 4 2 1 -> 경로



#1
#7 8
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


# V n으로 바꾸기
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
'''
#
# def KFC(x):
#     if x == 2:
#         return
#
#     print(x)
#     KFC(x + 1)
#     print(x)
#
#
# KFC(0)
# print('끝')


# def BGK(x):
#     if x == 6:
#         return
#     print(x, end=" ")
#     BGK(x+1)
#     print(x, end=" ")
#
# BGK(0)


def Tree(x):
    if x == 3:
        return

    for i in range(2):
        Tree(x+1)

Tree(0)