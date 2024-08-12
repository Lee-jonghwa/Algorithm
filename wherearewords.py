def shipza(N, K):
    cnt = 0
    for i in range(N):
        for j in range(N):
            h = []  # 가로식
            v = []  # 세로식
            for k in range(K):  # 글자수에 대해서
                if arr[i][j] == 1 and 0 <= i + k < N and 0 <= j + k < N:
                    # 가로일 때
                    h.append([i][N-j-1])  # 한 열 다 돌았을 때
                    # 세로일 때
                    v.append([N-i-1][j])  # 글자 길이까지
            if h == K:  # h가 글자 길이와 같으면
                cnt += 1
            elif v == K:  # v가 글자 길이와 같으면
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(shipza(N, K))