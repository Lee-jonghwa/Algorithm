T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''
    for i in range(N):
        for j in range(N):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1] and len(arr[i][j:j+M]) == M:
                h = ''
                for k in range(M):
                    if j+k < N:
                        h += arr[i][j+k]
                        result = h
                break
            v= ''
            for k in range(M):
                if i+k < N:
                    v += arr[i+k][j]
            if v == v[::-1] and len(v) == M:
                result = v
                break
    print(f'#{tc}', result)