def calculate_risk(path, arr):
    total_risk = 0
    for i in range(len(path) - 1):
        total_risk += arr[path[i]][path[i+1]] # 연속된 두 외계인
    return total_risk

path = []
min_risk = float('inf')


# level: N, branch: N인 순열코드
def KFC(x):
    global min_risk
    if x == N:
        risk = calculate_risk(path, arr)
        if risk < min_risk:
            min_risk = risk
        return


    for i in range(N):
        if used[i] == True: continue
        used[i] = True
        path.append(i)
        KFC(x + 1)
        path.pop()
        used[i] = False


T = int(input())
for tc in range(1, N+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    used = [False for _ in range(N)]
    KFC(0)
    print(f'#{tc} {min_risk}')