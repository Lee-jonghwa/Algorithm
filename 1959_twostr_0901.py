T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_v = 0
    if N > M: # A가 더 길면
        for i in range(N-M+1):
            sum_v = 0
            for j in range(M):
                sum_v += A[i+j] * B[j]
            if max_v < sum_v:
                max_v = sum_v
    else: # B가 더 길면
        for i in range(M-N+1):
            sum_v = 0
            for j in range(N):
                sum_v += B[i+j] * A[j]
            if max_v < sum_v:
                max_v = sum_v

    print(f'#{tc} {max_v}')