def paperpaste(N):
    # n이 30 미만일 경우 직접 결과 반환
    if N < 30:
        return 1 if n == 10 else 3
    # dp 배열 초기화
    dp = [0] * (N + 1)
    dp[10] = 1
    dp[20] = 3
    for i in range(30, N, 10):
        # 점화식
        dp[i] = dp[i-10] + 2 * dp[i-20]
    return dp[N]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {paperpaste(N)}')
