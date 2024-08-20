
def min_button_press(n, target):
    cnt = 0
    # 인덱스 맞추기
    for i in range(1, n + 1):
        if target[i - 1] == 1:
            # 1을 발견하면-- > 카운팅
            cnt += 1
            # 배수만큼 켜거나 끔(1이면 0으로 0이면 1로)
            for j in range(i, n + 1, i): # 배수를 처리 하기 위한 step i
                target[j - 1] = 1 - target[j - 1]
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    target = list(map(int, input().split()))
    result = min_button_press(N, target)
    print(f'#{tc} {result}')