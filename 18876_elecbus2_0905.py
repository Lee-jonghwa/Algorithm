# 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 최소한의 교체 횟수로 목적지에 도착
# 마지막 정류장에는 배터리가 없다.


# dp접근

T = int(input())
for tc in range(1, T+1):
    # 충전소 위치는 N-1개
    M = list(map(int,input().split()))
    N = M.pop(0)
    M.append(0) # 도착점 추가
    # 이동 횟수를 저장하는 dp초기화
    dp = [float('inf')] * (2 * N)
    dp[0] = 0 # 첫자리는 0

    idx = 0
    move = 0
    while idx <= N-1: # 배열을 벗어나지 않는 선에서
        for i in range(1, M[idx]+1): # 갈 수 있는 범위 안에서 (되는 칸만큼 더 가므로 +1)
            dp[idx+i] = min(dp[idx+i],dp[idx]+1)
        idx += 1

    print(f'#{tc} {dp[N-1]-1}')


# bfs
"""
from collections import deque

def bfs(NM, N):
    global min_move

    q = deque()
    q.append((0,0)) # 시작점, 이동 횟수 넣기
    visited = [0] * N
    visited[0] = True

    while q: # q가 빌 때까지
        pos, moves = q.popleft() # 현재위치

        if pos == N-1: #도착하면
            min_move = min(min_move,moves)
            return

        if moves >= min_move:
            return

        for i in range(1, NM[pos] + 1):  # 충전기로 이동할 수 있는 용량까지
            if pos + i < N and not visited[pos + i]: # 내 자리가 N을 넘어가지 않을 떄
                visited[pos + i] = True
                q.append((pos + i, moves + 1)) # enqueue


T = int(input())
for tc in range(1, T+1):
    NM = list(map(int,input().split()))  # 충전기 위치
    N = NM.pop(0) # 정류장 수

    min_move = float('inf')

    bfs(NM, N)

    print(f'#{tc} {min_move-1}')
"""

"""
def dfs(lev, now, M):  # lev -> 횟수, now -> index
    global min_move

    if now >= N-1:  # 도착점에 왔으면
        min_move = min(min_move,lev)
        return

    if lev >= min_move:
        return

    for i in range(1, M[now] + 1):  # 한 칸 앞부터 가능 배터리 거리까지
        if now + i < N:
            dfs(lev+1, now+i, M)

T = int(input())
for tc in range(1, T+1):
    NM = list(map(int,input().split()))  # 충전기 위치
    N = NM.pop(0) # 정류장 수

    min_move = 100

    dfs(0,0,NM)

    print(f'#{tc} {min_move}')
"""