# N 배수로 양 세기

# 첫 번째에는 N번 양을 세고, 두 번째에는 2N번 양, … , k번째에는 kN번 양을 센다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    used = [0] * 10 # 0~9까지 사용됐는지 확인하는 배열
    cnt = 0
    sheeps = N # 첫 양 N
    while True: # N이 유효한 동안
        if sum(used) == 10: # 모두 사용되면
            break
        temp = sheeps
        for _ in range(len(str(sheeps))): #N의 자리수 만큼
            used[temp%10] = 1 # 1의 자리수 만큼 줄임
            temp = temp//10
        cnt += 1
        sheeps += N


    print(f'#{tc} {cnt*N}')