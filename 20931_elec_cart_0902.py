
# 1번은 사무실을, 2번부터 N번은 관리구역 번호

# 1 로 시작하는 모든 순열 구해서 합을 함

def search_min_v(path):
    global min_v
    sum_v = 0
    for i in range(1, len(path)):
        y = path[i-1]
        x = path[i]
        sum_v += arr[y][x]
    # 마지막으로 다시 사무실(0번)로 돌아오는 경로의 배터리 소비량 추가
    sum_v += arr[path[-1]][0]
    if min_v > sum_v:
        min_v = sum_v


def elec_cart(lev):

    if lev == N: # 3 번 순열, 시작이 1인 경우
        search_min_v(path)
        return

    for i in range(1, N): # 사무실 제외 순회
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        elec_cart(lev+1)
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_v = float('inf')
    used = [0]*N
    path = [0] # 사무실 시작

    elec_cart(1) # 사무실부터 시작이므로 1 에서 부터 시작
    print(f'#{tc}',min_v)

