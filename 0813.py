"""
N = 10
q = [0] * 10
front = -1
rear = -1

# euQueue(1)
rear += 1
q[rear] = 1
# euQueue(2)
rear += 1
q[rear] = 2
# euQueue(3)
rear += 1
q[rear] = 3

print(q)  # [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]

# deQueue()
front += 1
print(q[front])  # 1
front += 1
print(q[front])  # 2
front += 1
print(q[front])  # 3

q2 = []
q2.append(10)
q2.append(20)

print(q2.pop(0))  # 10
print(q2.pop(0))  # 20
print(q2)  # []
"""

"""
cQ = [0] * 4
front = rear = 0
cQ_Size = 4

# enQueue(1)
rear = (rear + 1) % cQ_Size
cQ[rear] = 1
# enQueue(2)
rear = (rear + 1) % cQ_Size
cQ[rear] = 2
# enQueue(3)
rear = (rear + 1) % cQ_Size
cQ[rear] = 3

print(cQ)  # [0, 1, 2, 3]

# deQueue()
front = front + 1
print(cQ[front])  # 1

# deQueue()
front = front + 1
print(cQ[front])  # 2

# deQueue()
front = front + 1
print(cQ[front])  # 3


# enQueue(10)
rear = (rear + 1) % cQ_Size
cQ[rear] = 10

# enQueue(20)
rear = (rear + 1) % cQ_Size
cQ[rear] = 20

print(cQ)  # [10, 20, 2, 3]
"""

"""
from collections import deque

list_q = []
for i in range(1000000):
    list_q.append(i)
for _ in range(1000000):
    list_q.pop(0)
print('end')

deque_q = deque()
for i in range(1000000):
    deque_q.append(i)
for _ in range(1000000):
    deque_q.popleft()
print('end')
"""


"""

1. 큐
queue: FIFO
enqueue, dequeue
enqueue: append() 메서드
dequeue: pop(0) => 시간복잡도 O(n)으로 높음 ==> deque


* 덱 모듈
collections.deque 사용 --> deque 별도 생성 필요

enqueue: append() 메서드
deque: popleft() 메서드
시간복잡도: O(1)
***스택과 큐의 서술형 문제 대비 필요!***


2. 우선순위 큐(큐와 다른 것으로 생각!)
heap 모듈 사용
enqueue: heapq.heappush(heap, item): 새로운 요소를 우선순위에 따라 적절한 위치에 추가
dequeue: heapq.heappop(heap): 가장 높은 우선순위를 가진 요소를 제거 및 반환
시간복잡도: O(logN) -> O(1)과 거의 유사
"""