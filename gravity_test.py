def gravity(N):
    max_v = 0
    for i in range(N):
        fall = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                fall += 1
        if fall > max_v:
            max_v = fall
    return max_v


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {gravity(N)}')