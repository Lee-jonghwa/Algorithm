'''
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_lst = sorted(list(map(int, input())))
    cards_dict = {}
    max_card = {}
    for i in num_lst:
        if i in cards_dict:
            cards_dict[i] += 1
        else:
            cards_dict[i] = 1
        for k, v in cards_dict.items():
            if max(cards_dict.values()) == v:
                max_k = k
                max_v = v
    print(f'#{tc} {max_k} {max_v}')
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a = list(map(int, input()))

    cnt = [0] * 10 # 각 숫자별 카드 갯수 배열 초기화
    for j in range(N):
        cnt[a[j]] += 1 # 해당 숫자 카드의 개수 증가
    result = 0 # 현재 가장 많이 발견된 카드의 갯수
    for k in range(10):
        if result <= cnt[k]:
            result = cnt[k] # 가장 많은 카드의 개수
            idx = k # 가장 많은 카드의 숫자

    # 1. cnt[k]가 result보다 큰 경우 : 더 많은 카드를 발견한 경우
    # 2. cnt[k]가 result와 같은 경우 : 같은 개수의 카드이지만, 더 큰 숫자의 카드를 우선시
    # ==> cnt[k] >= result

    print(f'#{tc} {idx} {result}')