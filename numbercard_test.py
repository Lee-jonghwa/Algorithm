def numcard(N):
    lst = [0] * 10 # 요소 10개 제한
    for i in range(N):
        lst[arr[i]] += 1
    cnt = 0
    for j in range(10):
        if lst[j] >= cnt:
            cnt = lst[j]
            idx = j
    return idx, cnt




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    print(f'#{tc}', *numcard(N))