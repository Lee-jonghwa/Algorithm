T = int(input())
for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    answer_arr = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = float('-inf')
    min_v = float('inf')
    for n in range(N):
        cnt = 1
        score = 0
        for m in range(M):
            if answer_arr[m] == arr[n][m]:
                score += cnt
                cnt += 1
            else:
                cnt = 1

        max_v = max(max_v, score)
        min_v = min(min_v, score)

    result = max_v - min_v
    print(f'#{tc} {result}')



"""

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

"""