def KFC(x, cur_sum):
    global min_sum, N
    if x == N: # 탐색을 마치면
        min_sum = min(min_sum, cur_sum)
        return

    if cur_sum >= min_sum: #현재 합이 이미 최소합 보다 클 때
        return

    for i in range(N):
        if used[i]: continue
        used[i] = 1
        path.append(arr[x][i])
        KFC(x + 1, cur_sum + arr[x][i])
        path.pop()
        used[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    path = []
    min_sum = float('inf')
    KFC(0, 0)
    print(f'#{tc} {min_sum}')

'''
def arr_min(arr, N, s, sum_v): # lev 3이면 종료, s: 시작점, sum : 합 branch N
    global min_sum
    if s == N: # N번째까지 숫자를 고르면
        if sum_v < min_sum:
            min_sum = sum_v

    # 현재까지의 합이 이미 최소합을 넘는 경우, 더 이상 탐색할 필요가 없음
    if sum_v >= min_sum:
        return

    else:
        for j in range(N):
            if not used[j]: # 사용한 적 없으면
                used[j] = 1 # 흔적 남기기
                arr_min(arr, N, s+1, sum_v + arr[s][j])
                used[j] = 0 # 백트래킹 #다 돌고나서 흔적 지움


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = float('inf')
    arr_min(arr, N, 0, 0)
    print(f'#{tc} {min_sum}')
'''

'''
def bi_min(tar, s):
    result = 0
    for i in range(N):
        if tar & 0x1:
            result += arr[s][i] # 합산 값에 추가
        tar >>= 1 # 오른쪽으로 한 번 밀기
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = float('inf')
    for i in range(N):
        for tar in range(0, 1 << N): # N에 대한 arr list
            print(bi_min(tar,i))
'''


'''
def arr_min(s, csum, used_j):
    global min_sum, N, arr

    if s == N:
        min_sum = min(min_sum, csum)
        return

    # 현재까지의 합이 이미 최소합을 넘는 경우, 더 이상 탐색할 필요가 없음
    if csum >= min_sum:
        return

    # 현재 행에서 가능한 모든 열을 선택
    for j in range(N):
        if not (used_j & (1 << j)):  # 해당 열이 아직 선택되지 않았으면
            arr_min(s + 1, csum + arr[s][j], used_j | (1 << j))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    arr_min(0, 0, 0)  # 초기 호출: row=0, current_sum=0, used_columns=0

    print(f"#{tc} {min_sum}")
'''

'''
비트마스크를 통한 열 선택 추적:

used_columns는 현재까지 선택된 열을 비트마스크로 나타냅니다. 예를 들어, used_columns의 값이 0b00101이라면 0번 열과 2번 열이 이미 선택된 것입니다.
재귀적 탐색:

arr_min(row, current_sum, used_columns) 함수는 row 행에서 가능한 모든 열을 탐색하며, 열 선택이 중복되지 않도록 추적하면서 재귀적으로 최소합을 계산합니다.
최소합 계산:

모든 행을 탐색한 후, 계산된 current_sum이 min_sum보다 작으면 이를 갱신합니다.
재귀 호출:

각 재귀 호출에서는 row를 1씩 증가시키며 다음 행으로 넘어가고, current_sum에 현재 선택된 열의 값을 더한 후, used_columns에 현재 선택된 열을 기록하여 중복 선택을 방지합니다.
'''