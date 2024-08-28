'''
7
20 15 19 4 13 11 17

7
20 15 19 4 13 11 23
'''
import heapq
from heapq import heappush, heappop

N = int(input())          # 필요한 노드 수
arr = list(map(int, input().split()))

heap = []  # 최대힙을 구현하기 위한 리스트

# 최소힙 ( 기본 )
for num in arr:
    heappush(heap, num)

print([x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(heappop(heap), end=' ')

print('\n------------------------------------')

# 최대힙
# 삽입 시 음수로 곱하여 저장 (제일 큰 수가 제일 작아짐)
# 삭제 후 음수값을 곱하여 출력 (다시 원래 수로 복구하여 출력)
for num in arr:
    heappush(heap, -num)

print([-x for x in heap])  # 힙의 내부 상태를 출력 (음수로 저장된 상태)

while heap:
    print(-heappop(heap), end=' ')





heap2 = []
heappush(heap2, 4) # heap == [4]
heappush(heap2, 1) # 1이 4보다 작으므로 root에 위치 -> heap == [1, 4]
heappush(heap2, 7) # 7이 가장 크므로 마지막에 위치 -> heap == [1, 4, 7]
heappush(heap2, 3) # 3이 4보다 작으므로 4와 자리를 바꿈 -> heap == [1, 3, 7, 4]

print(heap2)

# heappush: 새 항목을 추가하면서 자동으로 우선순위에 맞게 정렬


# heappop: 힙에서 가장 작은 원소를 제거하고 반환
print(heapq.heappop(heap2)) # 1
print(heapq.heappop(heap2)) # 3
print(heapq.heappop(heap2)) # 4
print(heapq.heappop(heap2)) # 7

