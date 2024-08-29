# dp 배열은 그 자리에 도착했을 때의 총점으로 생각하기


N = int(input())
A = tuple(map(int, input().split()))
A = (0,) + A + tuple(0 for _ in range(5)) # 인덱스 에러 방지(첫자리 추가, 뒤 6자리 추가)

# 최대 점수 dp테이블 초기화
dp = [float('-inf')] * (N + 6) # 점프 고려
dp[0] = 0  # 시작 지점 0

# 처음 7칸은 2칸 점프로 도달할 수 있는 위치 -> 점수 계산
for i in range(2, 8):
    dp[i] = dp[i-2] + A[i] # 기본 점수에서 2칸 뛴 점수 더함

# 7번째는 7칸 점프
dp[7] = A[7]

# 8번째 부터
for i in range(7, N + 6):
    # 7칸 점프 / 2칸 점프
    dp[i] = max(dp[i-7] + A[i], dp[i-2] + A[i])

# 도착 가능한 위치중 가장 최고 점수
print(max(dp[N:]))

"""
GPT


def max_score(n, score_map):
    # DP 테이블 초기화
    dp = [-float('inf')] * n  # 초기값을 매우 작은 수로 설정
    dp[0] = score_map[0]  # 첫 번째 칸에서 얻을 수 있는 점수

    # DP를 활용하여 각 칸에서 얻을 수 있는 최대 점수 계산
    for i in range(1, n):
        if i >= 2:
            dp[i] = max(dp[i], dp[i - 2] + score_map[i])
        if i >= 7:
            dp[i] = max(dp[i], dp[i - 7] + score_map[i])

    # 깃발에 도달했을 때 얻을 수 있는 최대 점수 반환
    return dp[-1]


# 입력
n = int(input())  # 맵 사이즈
score_map = list(map(int, input().split()))  # 각 칸의 점수

# 최고 점수 계산 및 출력
result = max_score(n, score_map)
print(result)
"""
"""
def max_score(n, scores):
    # DP 테이블 초기화
    dp = [-float('inf')] * n  # 각 칸에서의 최대 점수를 초기화
    dp[0] = scores[0]  # 시작 칸의 점수 설정

    # DP 상태 전이
    for i in range(n):
        if i + 2 < n:  # 짧은 점프 (2칸)
            dp[i + 2] = max(dp[i + 2], dp[i] + scores[i + 2])
        if i + 7 < n:  # 긴 점프 (7칸)
            dp[i + 7] = max(dp[i + 7], dp[i] + scores[i + 7])

    # 최대 점수를 반환
    return max(dp)

# 입력 처리
n = int(input("맵 사이즈 n을 입력하세요: "))  # 맵 사이즈
scores = list(map(int, input("맵 정보를 입력하세요: ").split()))  # 점수 정보

# 최대 점수 계산 및 출력
result = max_score(n, scores)
print(result)
"""



def mario(n):
    dp = [float('-inf')] * (n + 1) # 각 위치의 점수
    dp[0] = 0

    # 가능한 모든 경우를 계산
    for jump in jumps:
        dp[jump] = max(dp[jump], dp[jump])

    return dp[n]

n = int(input())  # 맵 길이
arr = list(map(int, input().split()))
# 점프는 2칸 또는 7칸
jumps = [2, 7]