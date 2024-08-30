import heapq

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heap = []
    sum_v = 0 # 조상노드 총합
    # tree 그리기
    for num in map(int,input().split()):
        heapq.heappush(heap, num)

    # 조상 찾기
    idx = N - 1 #최대 인덱스 맞추기
    while idx > 0: # heap을 벗어나지 않는 선에서
        idx = (idx - 1)//2 # 반올림 하지 않도록 만들기
        sum_v += heap[idx]

    print(f'#{tc} {sum_v}')


"""
import heapq
from heapq import heappush, heappop

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = []
    for num in map(int,input().split()):
        heappush(tree, num) # 자동으로 우선순위 정렬

    sum_v = 0
    N = len(tree) // 2 # 트리의 마지막 노드의 부모 노드 인덱스
    while N:
        sum_v += tree[N-1]
        N //= 2 # 부모노드로 올라감

    print(f'#{tc} {sum_v}')

"""

"""
'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''

import heapq
from heapq import heappush, heappop



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = []  # 최대힙을 구현하기 위한 리스트

    # 최소힙 ( 기본 )
    for num in arr:
        heappush(heap, num)

    # 마지막 노드 heap(N)
    # 그 조상은 N //2

    # 인덱스 맞추기
    idx = N - 1
    sum_v = 0

    while idx > 0:
        idx = (idx - 1) // 2
        sum_v += heap[idx]

    print(f'#{tc} {sum_v}')
"""