# Queue, Greedy

from collections import deque

def cost(N, M1, M2, blocks):
    blocks.sort(reverse=True)
    blocks = deque(blocks)
    tower1 = []
    tower2 = []
    while blocks:
        # 첫 번째 탑 채우기
        if len(tower1) < M1:
            weight = blocks.popleft()
            tower1.append([weight, len(tower1) + 1])

        # 두 번째 탑 채우기
        if len(tower2) < M2:
            weight = blocks.popleft()
            tower2.append([weight, len(tower2) + 1])
    # 비용계산
    cost1 = sum(weight * cnt for weight, cnt in tower1)
    cost2 = sum(weight * cnt for weight, cnt in tower2)

    return cost1 + cost2

T = int(input())
for tc in range(1,T+1):
    N, M1, M2 = map(int, input().split())
    blocks = list(map(int, input().split()))
    result = cost(N, M1, M2, blocks)
    print(f'#{tc} {result}')

"""
# queue 활용
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M1, M2 = map(int, input().split()) # N: 총 블록의 종류 M1: 첫번째 탑 블록 종류 M2: 두 번째 탑 블록
    blocks = deque(sorted(map(int, input().split()), reverse=True))
    sum_v = 0
    for i in range(1, min(M1,M2)+1):
        sum_v += blocks.popleft() * i
        sum_v += blocks.popleft() * i
    if M2 > M1:
        for j in range(M1+1, M2+1):  # 이후부터 나머지
            sum_v += blocks.popleft() * j
    else:
        for j in range(M2+1, M1+1):  # 이후부터 나머지
            sum_v += blocks.popleft() * j

    print(f'#{tc} {sum_v}')

    # 주어진 블록 모두 사용하면서도 비용 최소화
    # 블록의 무게가 곧 비용
    # 사용하는 블록 수 오름차순 --> 큰 게 앞, 작은게 뒤 사용 -> 젤 앞에 있는 건 뭔지 상관 없음
    # 최대 갯수는 M 최대 개수
    # 블록의 종류가 중복되면 안 됨
"""