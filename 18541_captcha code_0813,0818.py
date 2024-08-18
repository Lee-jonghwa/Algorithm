
# 랜덤으로 N개 길이의 Sample이 주어진다.
# 그리고 K개 길이의 PassCode가 주어진다.
# 사용자는 Sample에서 PassCode를 "순차적으로" 만들 수 있는지를 검증해야 한다.
# 첫번째 줄에는 Sample의 길이 N, PassCode의 길이 K가 주어진다.
# 두번째 줄에는 N개 길이의 Sample이 공백으로 구분되어 주어진다.
# 세번째 줄에는 K개 길이의 PassCode가 공백으로 구분되어 주어진다.

def captch():
    start = 0
    for code in pc: # 패스코드 하나를 가지고
        idx = smp.find(code, start)
        if idx == -1:
            return 0
        else:
            start = idx +1

    return 1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    smp = input() # find 쓰기위해 문자열로 받음
    pc = input()
    result = captch()
    print(f'#{tc} {result}')


"""
def captcha(sample, passcode):
    start = 0
    for code in passcode:
        idx = sample.find(code, start) # 찾은 자리
        if idx == -1:  # find에서 못 찾았을 때
            return 0
        start = idx + 1

    return 1

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = input()  # find 쓸 것이므로 그대로 받음
    passcode = input()
    result = captcha(sample, passcode)
    print(f'#{tc} {result}')
"""

"""
def captcha(N, K, sam, pc):
    result = [0]
    for j in range(K):  # 모든 키 값 순회
        for i in range(N):  # 모든 샘플 값 순회
            if pc[j] == sam[i]:  # 값 비교
                if i > result[-1]:  # 순차적으로 큰 값
                    result.append(i)  # idx 추가
                    break  # 더 이상 순회 x

    if len(result) - 1 == K:  # 갯수가 같으면
        return 1  # 1 리턴
    else:  # 갯수가 다르면
        return 0  # 0 리턴

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sam = list(map(int, input().split()))
    pc = list(map(int, input().split()))
    print(f'#{tc} {captcha(N, K, sam, pc)}')
"""