# 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용

def dfs(lev, cur_cost): # 순열 접근
    global min_v
    if lev == N:
        min_v = min(min_v, cur_cost)
        return

    if cur_cost >= min_v:
        return

    for i in range(N): # 세가지 제품
        if visited[i]: continue
        visited[i] = 1
        dfs(lev + 1, cur_cost + arr[lev][i])
        visited[i] =0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =  [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    min_v  = 99*4

    dfs(0,0)
    print(f'#{tc} {min_v}')