def fibo(n):
    dp = [0] * (n + 1) # 가능한 모든 경우의 dp 생성
    dp[0] = 0
    dp[1] = 1
    # 0부터 시작하므로 range범위가 n
    for i in range(2, n): # 1은 있으니, 2부터 n까지를 더하기
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n-1]

n = int(input())
result = fibo(n)
print(result)

"""

# 메모이제이션을 사용한 피보나치 수열
def fib_memo(n, memo={}):
    if n in memo:  # 이미 계산한 값이 있다면 반환
        return memo[n]
    if n <= 1:  # 피보나치 수열의 기본 케이스
        return n
    # 피보나치 계산 및 메모에 저장
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# 예시: 피보나치 수열의 10번째 값을 구하기
print(fib_memo(10))  # 출력: 55
"""