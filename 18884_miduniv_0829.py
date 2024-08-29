'''
최대힙, 최소힙
최대힙
1. 부모노드 >= 자식노드
2. 루트 노드 가장 큰값

최소힙
1. 부모노드 <= 자식노드
2. 루트 노드 가장 작은값
'''

import heapq

max_heap = []
min_heap = []
mid = 500

def push(v):
    if mid > v:
        heapq.heappush(max_heap, -v) # 최대 힙이므로 - 곱함
    else:
        heapq.heappush(min_heap, v)

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    push(a)
    push(b)

    if len(max_heap) > len(min_heap):
        heapq.heappush(min_heap,mid)
        mid = -heapq.heappop(max_heap) # 가장 작은 값 빼기
    elif len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -mid)
        mid = heapq.heappop(min_heap) # 가장 작은 값 빼기

    print(mid)


"""
GPT

# 중앙값을 구할 땐 최대힙과 최소힙을 양쪽에 다는 방법 사용


import heapq

# 최대 힙 (작은 절반을 저장)
max_heap = []

# 최소 힙 (큰 절반을 저장)
min_heap = []

# 초기 중앙값 설정
median = 500
heapq.heappush(max_heap, -median) # 최대 힙 사용 시 -달기

N = int(input())  # 사람수

for _ in range(N):
    a, b = map(int, input().split()) # 매번 받을 때마다 힙 업데이트

    # 새로운 값을 적절한 힙에 삽입
    if a > -max_heap[0]: # 가장 최대값이 아니라면
        heapq.heappush(min_heap, a)
    else: # 최소값 힙으로 반영
        heapq.heappush(max_heap, -a)

    if b > -max_heap[0]: # b도 동일
        heapq.heappush(min_heap, b)
    else:
        heapq.heappush(max_heap, -b)

    # 힙 길이 갖게 하기 -> 중앙값 맞추기
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    # 현재 중앙값은 max_heap의 루트 값
    median = -max_heap[0]
    print(median)
"""
