


def min_coins(T, coins):
    # DP 테이블 초기화: dp[i]는 i 금액을 만들기 위한 최소 동전 개수
    dp = [float('inf')] * (T + 1)
    dp[0] = 0  # 0원을 만드는 데는 동전이 0개 필요

    # 동전으로 가능한 모든 경우를` 계산
    for coin in coins:
        for i in range(coin, T + 1): # 목표 금액까지의 모든 금액
            # dp테이블에 저장, 최소 동전의 개수 업데이트
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # T원을 만들 수 있는지 확인
    if dp[T] == float('inf'): # 끝까지 갔는데 안 되면
        return "impossible" # 불가능
    else:
        return dp[T]

# 입력 받기
T, n = map(int, input().split()) # T: 물건 총액, n: 동전 종류
coins = list(map(int, input().split())) # 동전 개수

# 최소 동전 개수 출력
result = min_coins(T, coins)
print(result)