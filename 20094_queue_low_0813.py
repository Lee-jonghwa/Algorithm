from collections import deque


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    deque_q = deque(map(int, input().split()))  # 리스트 대신 덱으로 감싸면 됨

    for i in range(M):
        deque_q.append(deque_q.popleft())

    result = deque_q[0]  # 디버깅을 위해 result를 따로 해두는 게 좋음

    print(f'#{tc} {result}')

