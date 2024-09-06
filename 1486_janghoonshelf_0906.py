import sys
sys.stdin = open('1486_input','r')


# 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 한다.

# idx: 지금 세울 사람
def subset_sum(idx, sum_v):
    global min_v

    # 종료조건
    if sum_v >= B: # B가 넘어가면
        if min_v > sum_v:
            min_v = sum_v #최소값 초기화

    # 다 순회했을 때
    if idx == N: # 모든 후보를 돌면
        return

    # 다음 애를 세운다
    subset_sum(idx+1, sum_v + heights[idx])

    # 다음 애를 안 세운다
    subset_sum(idx+1, sum_v)


T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    heights = list(map(int,input().split()))

    min_v = 1e9
    # 세우는 모든 경우이므로 부분집합의 합
    subset_sum(0, 0)

    print(f'#{tc} {min_v - B}')

"""
# 부분집합의 합
# 탑의 높이는 점원이 1명일 경우 그 점원의 키와 같고, 2명 이상일 경우 탑을 만든 모든 점원의 키의 합과 같다.

# 숨겨진 조건: 모든 점원을 쌓았는데 B이하인 경우

# 시작점 0번 점원 / 탑의 높이는 0부터


def recur(cnt, sum_height):
    global ans
    # 가지치기: 이미 탑의 높이가 B 이상 -> 적절한 값을 고려할 수 없음
    if sum_height >= B:
        ans = min(ans, sum_height)
        return

    if cnt == N: # 모든 점원을 탑을 쌓는데 고려했다면
        return

    # cnt 번 점원을 탑에 쌓는다
    recur(cnt + 1, sum_height + heights[cnt])

    # 탑에 안 쌓는다,
    recur(cnt + 1, sum_height)


T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    heights = list(map(int,input().split()))

    ans = 1e9 # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장
    # 최대값부터 점점 낮춰주기

    recur(0,0)
    print(f'#{tc} {ans - B}')
"""
