T = int(input())
for tc in range(1, T+1):
    n = float(input())
    cnt = 0
    bin = ""
    while n > 0:
        temp = n * 2
        bin += str(temp)[0] # 정수 부분을 이진수 문자열에 추가
        n = temp - int(temp)
        cnt += 1
        if cnt > 12: # 이진수 자리수가 12자리 넘어가면
            break

    if cnt > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {bin}')



"""
def float_bi(N):
    num = N
    bi_num = ""
    while num > 0:
        if len(bi_num) == 13:  # 13자리가 되면
            return "overflow"

        num *= 2
        bi_num += str(int(num // 1)) # 1의 자리 값에 넣기
        num = num % 1
    return bi_num


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = float_bi(N)
    print(f'#{tc} {result}')
"""