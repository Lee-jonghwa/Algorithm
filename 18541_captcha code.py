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