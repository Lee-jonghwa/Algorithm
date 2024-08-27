"""
# 투 포인트 알고리즘
a = 맨처음
b = 중간 + 1

loop {
    a 출력 후 a += 1
    b 출력 후 b += 1
}
"""

def twopoint():
    a = 0
    b = (N + 1) // 2

    for turn in range(len(arr)):
        if turn % 2 == 0:
            print(arr[a], end =" ")
            a += 1
        else:
            print(arr[b], end = " ")
            b += 1

"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    print(f'#{tc} ', end= "")
    twopoint()
    print()


def twopoint(cards,N):
    a = 0
    b = N // 2 + N % 2

    new_cards = []
    while len(new_cards) < N:
        if a < b: # 중간 가기 전까지
            new_cards.append(cards[a])
            a += 1
        if b < N: # 배열 끝까지
            new_cards.append(cards[b])
            b += 1

    return new_cards


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    result = twopoint(cards, N)
    print(f'#{tc}', *result)
"""


"""
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())

    deck = [0] * N

    d = (N + 1) // 2 # 아래 오는 카드 시작 N//2 + N%2

    i1 = 0
    i2 = d
    i3 = 0 # 새로 만들 댁
    while i3 < N: # 셔플이 끝나기 전이면
        if i1 < d:
            deck[i3] = card[i1]
            i1 += 1
            i3 += 1
        if i2 < N:
            deck[i3] = card[i2]
            i2 += 1
            i3 += 1

    print(f'#{tc}', *deck)
"""