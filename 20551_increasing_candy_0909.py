import sys
sys.stdin = open('20551_input.txt','r')


# 세 개의 상자를 나란히 각 상자에 들어 있는 사탕의 개수가 순증가
# 모든 상자에 1개 이상의 사탕이 들어 있기를 원한다.
# 상자 속에 들어 있는 사탕을 (0개 이상) 먹어 없애 버리는 것이다
# 최소 몇 개의 사탕을 먹어야 하는지

def increasing_candy(A,B,C):
    eat_candy = 0

    if B < 2 or C < 3: # 무조건 0이 되는 조건일 때
        return -1

    # A 가  B - 1 이되고, B가 C - 1이 되는 조건일 때 최소
    # 이미 순서대로 되어있으면 안 먹는 게 베스트
    # A부터 하면 변동이 또 생기므로 반대로 C부터 하기

    # B에 있는 상자가 같거나 크면 -> 먹어줘야함
    if B >= C:
        # 최소가 되도록 먹기
        eat_candy += B - (C - 1)
        # B 자리 옮기기
        B = C - 1
    if A >= B:
        eat_candy += A - (B - 1)
        A = B - 1

    return eat_candy



T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int,input().split())

    result = increasing_candy(A, B, C)

    print(f'#{tc} {result}')





"""
T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # 1≤A,B,C≤3000
    # A < B < C 구조 만들 수 없을 때
    # -> A가 1, B가 2, C가 3일때가 최소
    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat = 0  # 먹은 사탕 개수
    # 설계: B가 C 이상일 때, B = C - 1이라면 최소
    if B >= C:
        eat += B - (C - 1) # 차이만큼 먹음
        B = C - 1 # 초기화

    # A 가 B 이상일 때 A = B - 1 이라면 최소
    if A >= B:
        eat += A - (B - 1)
        A = B - 1


    print(f'#{tc} {eat}')
"""