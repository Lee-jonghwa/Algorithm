# triplet or run 확인
def check_win(cards):
    cnt = [0] * 10
    for num in cards:
        cnt[num] += 1 # 카드 숫자 세기
    # triplet 확인
    if 3 in cnt:
        return True
    # run 확인
    for i in range(8):
        if 0 not in cnt[i : i + 3]:
            return True
    return False

# 플레이어 1 승리 or 플레이어 2 승리 or 무승부
def winner(all_cards):
    p1 = [] # 플레이어1 카드
    p2 = [] # 플레이어2 카드
    for i in range(6):
        p1.append(all_cards[i * 2]) # 플레이어1에 카드 추가
        if len(p1) > 2 and check_win(p1): # (triplet이거나 run) 이고 카드가 3장이상
            return 1 # 플레이어 1 승리

        p2.append(all_cards[i * 2 + 1]) # 플레이어2에 카드 추가
        if len(p2) > 2 and check_win(p2): # (triplet이거나 run) 이고 카드가 3장이상
            return 2 # 플레이어 2 승리

    return 0 # 무승부

T = int(input())
for tc in range(1, T + 1):
    all_cards = list(map(int, input().split()))
    result = winner(all_cards)
    print(f'#{tc} {result}')

# 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개
# 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
# 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다

# 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오.
# 만약 무승부인 경우 0을 출력
"""
def babegin(cards):
    # 카드 개수 체크
    card_cnt = [0] * 10

    for card in cards:
        card_cnt[card] += 1

    # triplet 확인
    for count in card_cnt:
        if count >= 3:
            return True

    # run 확인
    for i in range(8):  # 0 ~ 7까지 확인 (8, 9는 3연속이 될 수 없음)
        if card_cnt[i] >= 1 and card_cnt[i + 1] >= 1 and card_cnt[i + 2] >= 1:
            return True

    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    result = 0
    a_cards = []
    b_cards = []

    for i in range(0,12,2):  # 6번씩 플레이어가 카드를 가져간다.
        a_cards.append(cards[i])
        if babegin(a_cards):
            result = 1
            break

        b_cards.append(cards[i+1])
        if babegin(b_cards):
            result = 2
            break

    print(f'#{tc} {result}')
"""