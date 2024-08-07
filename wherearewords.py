def shipza(N, K):
    cnt = 0
    for i in range(N):
        for j in range(N):
            h = 0
            v = 0
            for k in range(K):
                if arr[i][j] == 1 and 0 <= i + k < N and 0 <= j + k < N:
                    #가로일 때
                    h += arr[i][j+k]
                    #세로일 때
                    v += arr[i+k][j]
            if h == K:
                cnt += 1
            elif v == K:
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(shipza(N, K))