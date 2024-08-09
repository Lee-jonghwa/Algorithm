def sum_sub(arr, N, S): # arr에서 합계 구하기, S는 목표합계
    cnt = 0 # 10 만족하는 값 찾기
    for tar in range(1, 1<<N): # 공집합을 제외한
        sub_sum = 0
        for i in range(N):
            if tar & 0x1: # target과의 & 연산자가 True 인 경우
                sub_sum += arr[i]
            tar >>= 1
        # sub_sum과 목표합이 같으면 cnt
        if sub_sum == S:
            cnt += 1
    return cnt



T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split()) # N은 원소개수, S 는 총합
    arr = list(map(int,input().split()))
    print(f'#{tc} {sum_sub(arr, N, S)}')