T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    #각각은 총 N개의 행
    turn_90 = [""]*N # 각 열의 요소를 행마다 추가
    turn_180 = [""]*N # 각 행의 요소를 역순으로 추가
    turn_270 = [""]*N # 각 열의 요소를 행마다 추가하되 turn 90의 역순

    for j in range(N):
        for i in range(N-1,-1,-1):
            turn_90[j] += arr[i][j]

    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            turn_180[N-1-i] += arr[i][j]

    for j in range(N-1,-1,-1):
        for i in range(N):
            turn_270[N-1-j] += arr[i][j]

    print(f'#{tc}')
    for k in range(N):
        print(turn_90[k], turn_180[k], turn_270[k])
