# 각 블록은 무게와 그에 따른 비용이 있다. 블록의 무게가 곧 그 블록을 사용하는 비용
# 전체 비용을 최소
# 4. 첫 번째 탑에서는 블록의 개수가 1, 2, 3, ... 순으로 오름차순이어야 한다.
# 5. 두 번째 탑에서도 블록의 개수가 1, 2, ... 순으로 오름차순이어야 한다.
# 모든 주어진 블록을 반드시 사용


# 개수가 오름차순이므로, 큰 값을 가장 적게 사용하는 게 좋음
# 2. M1 + M2 = N

# 각 테스트 케이스의 첫째 줄에는 N, M1, M2가 주어지고, 둘째 줄에는 각 블록의 무게가 주어진다.
# N : 총 블록의 종류 수
# M1 : 첫 번째 탑에 사용해야 하는 블록의 종류 수
# M2 : 두 번째 탑에 사용해야 하는 블록의 종류 수

# 다 사용하면서도 갯수를 줄이는 게 좋음

from collections import deque

def two_towers():
    # 타워별 리스트
    tw1 = []
    tw2 = []

    # 블록을 역순으로 정렬

    sum_tw1 = 0
    sum_tw2 = 0

    i = 0
    while blocks:   # 블록이 있는 동안
        i += 1  # 오름차순 반영 위한 세팅

        if i <= min(M1,M2): # 두 개 겹치는 범위 까지는
            # 둘 다 넣음
            tw1.append(blocks.popleft() * i)
            tw2.append(blocks.popleft() * i)

        else:   # 그 범위를 넘어가면
            if M1 > M2:
                tw1.append(blocks.popleft() * i)
            if M2 > M1:
                tw2.append(blocks.popleft() * i)

    # 각 리스트 값 더하기
    for j in tw1:
        sum_tw1 += j
    for k in tw2:
        sum_tw2 += k

    return sum_tw1 + sum_tw2

T = int(input())
for tc in range(1,T+1):
    N, M1, M2 = map(int, input().split())
    # 역순으로 정렬된 덱으로 사용
    blocks = sorted(list(map(int, input().split())), reverse=True)
    blocks = deque(blocks)


    result = two_towers()
    print(f'#{tc} {result}')



"""
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