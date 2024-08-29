# N 배수로 양 세기

# 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [0] * 10 # 0~9까지 사용됐는지 확인하는 배열
    cnt = 0
    num = 0
    while True: # N이 유효한 동안
        num += N
        div = num
        if sum(used) == 10: # 모두 사용되면
            break
        for _ in range(len(str(N))): #N의 자리수 만큼
            used[num%10] = 1
            num = num//10
        cnt += 1


    print(f'#{tc} {cnt}')