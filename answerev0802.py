def answer_ev(N, M, ans, arr):
    max_v = 0
    min_v = 100
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == ans[j]:
                cnt += 1  # 맟출 때 점수 부여
                # 연속할 때 가산 점
                for k in range(1, j):
                    if arr[i][j-k] == ans[j-k]:
                        cnt += 1
                    else:
                        break
        max_v = max(cnt, max_v)
        min_v = min(cnt, min_v)
    return max_v - min_v



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for i in range(N)]
    result = answer_ev(N, M, ans, arr)
    print(f'#{tc} {result}')