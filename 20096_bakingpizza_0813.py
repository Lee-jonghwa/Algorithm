from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 화덕크기 N, 피자 갯수 M
    cheeses = list(map(int, input().split()))  # 각 피자의 초기 치즈 양
    # 치즈의 양, 피자의 인덱스(1번 부터) ---> enumerate
    pizzas = deque([i + 1, p] for i, p in enumerate(cheeses))
    # 화덕
    oven = deque()
    for _ in range(N):  # 처음에 화덕에 피자를 N 개 넣음
        if pizzas:
            oven.append(pizzas.popleft())
    # 화덕에 피자가 한 개 남을 때까지 반복
    while len(oven) > 1:
        now = oven.popleft()  # 화덕에서 피자를 하나 꺼냄
        now[1] //= 2  # 꺼낸 피자의 치즈의 양 반으로 줄임

        if now[1] == 0:  # 치즈가 모두 녹았을 때,
            if pizzas:  # 남은 피자가 있으면
                oven.append(pizzas.popleft())

        else:  # 치즈가 아직 남아있을 때
            oven.append(now) # 다시 오븐에 넣음

    result = oven[0][0]

    print(f'#{tc} {result}')




"""
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 화덕의 크기, 피자개수 M
    C = list(map(int, input().split()))  # 피자 개수마다 올라간 치즈 # 인덱스 관리해야하기 때문에 덱 쓰지 않음
    deque_q = deque()  # 화덕

    for i in range(N):
        deque_q.append((i + 1, C[i])) # 인덱스를 기록하기 위한 튜플 자료 저장

    next_p = N  # 다음 피자 인덱스 -> 화덕 크기 만큼 반영

    while len(deque_q) > 1:
        num, piz = deque_q.popleft()  # 화덕의 첫 번째 피자를 꺼냄

        # 치즈를 녹임
        piz //= 2

        # 치즈가 다 녹지 않았으면 다시 화덕에 넣음
        if piz > 0:
            deque_q.append((num, piz))
        else:
            # 치즈가 다 녹았고, 남은 피자가 있다면 새 피자를 화덕에 넣음
            if next_p < M:  # 인덱스가 M 보다 작을 때
                deque_q.append((next_p + 1, C[next_p]))
                next_p += 1

    # 마지막으로 남은 피자의 번호 출력
    print(f"#{tc} {deque_q[0][0]}")



    # 치즈 양 C는 한 바퀴 돌 때 C//2

    # 원형 큐

    # 치즈가 모두 녹으면 화덕에서 꺼냄
    # 치즈의 양은 피자마다 다르기 때문에 꺼내지는 순서가 달라질 수 있음

    # 피자는 1번 위치에서 꺼냄 --> popleft()


    # 잠시 꺼내 치즈를 확인하고 같은자리 넣음

"""