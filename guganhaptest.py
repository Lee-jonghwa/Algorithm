def gugansum(N, M):
    max_v = 0
    min_v = float('inf')
    for i in range(N - M + 1): # N - M까지 순회
        sum_v = 0
        for j in range(M):
            sum_v += arr[i+j]
        max_v = max(max_v, sum_v)
        min_v = min(min_v, sum_v)
    return max_v - min_v



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {gugansum(N, M)}')