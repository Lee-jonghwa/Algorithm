# 두배를 곱하는 x2만큼은 정확하게 계산이 가능하다.
#  +1을 할때에, 끝에다가 1을 붙이는 식으로 계산을 하고 있다

# A, B가 있을때, A에서 x2 또는 +1 연산을 했을때 해당 숫자를 만들 수 있는가?


A, B = map(int, input().split())

# B의 끝자리를 1로 만듦
# 1을 없앰

# B에서 A로 가는 전략

tar = B
cnt = 0

while tar > A:
    # 2로 나눠지면
    if tar % 2 == 0:
        tar //= 2 # 2로 나눔
        cnt += 1

    else: #아니면
        if tar % 10 == 1:
            tar //= 10  # 1 붙이는 식
            cnt +=1
        else:
            cnt = -1
            break

print(cnt)