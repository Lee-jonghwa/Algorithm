import sys
sys.stdin = open('1952_input.txt','r')

# 수영장에서 판매하고 있는 이용권은 아래와 같이 4 종류이다.
# 1일 이용권 : 1일 이용이 가능하다.
# 1달 이용권 : 1달 동안 이용이 가능하다. 1달 이용권은 매달 1일부터 시작한다.
# 3달 이용권 : 연속된 3달 동안 이용이 가능하다. 3달 이용권은 매달 1일부터 시작한다.
#   (11월, 12월에도 3달 이용권을 사용할 수 있다)
# 1년 이용권 : 1년 동안 이용이 가능하다. 1년 이용권은 매년 1월 1일부터 시작한다.


# 모든 종류의 이용권 요금은 10 이상 3,000 이하의 정수
# 각 달의 이용 계획은 각 달의 마지막 일자보다 크지 않다.
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법

# 연권은 사면 무조건 1월
# dp가 좋아보이긴 한데

## 어쩄든 끝까지 가야하니, 순열 조합인 dfs 또는 일직선 진행이므로 dp접근


# 1. dfs
"""
def dfs(month, sum_v):
    global min_cost

    # 종료조건
    if month >= 12: # 11월에 3달 하는 경우도 있으므로 12 넘을 때 정지, 사실상 도착지점 12월
        if min_cost > sum_v:
            min_cost = sum_v
        return


    # 4개 조건
    # 1일치
    dfs(month+1, sum_v + schedule[month]*costs[0])
    # 한 달 -> 한 달부터는 일수 따질 필요 없음
    dfs(month+1, sum_v + costs[1])
    # 세 달
    dfs(month+3, sum_v + costs[2])
    # 1년
    dfs(month+12, sum_v + costs[3])
    return


T = int(input())
for tc in range(1, T+1):
    # 1일 / 1달 / 3개월 / 1년
    costs = list(map(int,input().split()))
    schedule = list(map(int,input().split()))

    min_cost = 1e10

    path = []
    visited = [0] * 13

    dfs(0, 0)

    print(f'#{tc} {min_cost}')
"""

# 2. dp


T = int(input())
for tc in range(1, T+1):
    # 1일 / 1달 / 3개월 / 1년
    costs = list(map(int,input().split()))
    schedule = [0] + list(map(int,input().split())) # 12 개월 맞추기

    min_cost = 1e10

    dp = [0] * 13 # 12월에 1년 하는 것 고려해 넉넉히, 비용이 발생하지 않으면 0원이므로 초기값 0


    for i in range(1, 13): # 1월~12월
        # 3개월 미만까지는 1개월 또는 1일
        dp[i] = min(dp[i-1] + (schedule[i] * costs[0]), dp[i-1] + costs[1])

        if i >= 3:
            dp[i] = min(dp[i-3] + costs[2], dp[i])


    result = min(dp[12], costs[3])
    print(f'#{tc} {result}')

# 시작점: 1월, 끝점: 12월
# 누적금액 가지고 가기

"""
def dfs(month, sum_cost):
    global ans

    if month > 12: #모든 달을 완료
        ans = min(sum_cost, ans)
        return


    # Tree형식으로 가기
    # 1일권 모두 구매 -> 다음달 확인
    dfs(month + 1, sum_cost + days[month] * costs[0])
    # 1달권 구매 -> 다음달 확인
    dfs(month + 1, sum_cost + costs[1])
    # 3달권 구매 -> 3달 후 확인
    dfs(month + 3, sum_cost + costs[2])
    # 1년권 구매 -> 12달 후 확인 => 재귀에서 뺴고 1월에 구입한 비용과 비교해도 됨
    dfs(month + 12, sum_cost + costs[3])

T = int(input())
for tc in range(1,T+1):
    costs = list(map(int,input().split()))
    days = [0] + list(map(int,input().split())) # 인덱스 맞추기
    ans = 1e9
    dfs(1, 0)
    print(f'#{tc} {ans}')
"""


# DP접근
"""
T = int(input())
for tc in range(1,T+1):
    costs = list(map(int,input().split()))
    days = [0] + list(map(int,input().split())) # 인덱스 맞추기
    dp = [0] * 13

    for i in range(1,13):
        # 1~ 2월까지 계산
        dp[i] = min(dp[i - 1] + (days[i] * costs[0]), dp[i - 1] + costs[1])

        # index 오류를 피하기 위해 3월 이후 따로
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + costs[2])


    result = min(dp[12], costs[3])
    print(f'#{tc} {result}')
"""