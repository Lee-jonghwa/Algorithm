def captcha(N, K, sam, pc):
    result = [0]
    for j in range(K):
        for i in range(N):
            if pc[j] == sam[i] and i >= result[-1]:
                result.append(i)
                continue
    if len(result) == K - 1:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sam = list(map(int, input().split()))
    pc = list(map(int, input().split()))
    print(f'#{tc} {captcha(N, K, sam, pc)}')
