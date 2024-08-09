
def sum_sub(arr, N, K): # arr에서 합계 구하기, K는 목표합계
    cnt = 0 # 10 만족하는 값 찾기
    for tar in range(1, 1<<12): # 모든 함수 반복
        sub_sum = 0
        sub_cnt = 0
        for i in range(12):
            if tar & 0x1: # target과의 & 연산자가 True 인 경우
                sub_sum += arr[i]
                sub_cnt += 1
            tar >>= 1
        # sub_sum과 목표합이 같으면 cnt
        if sub_cnt == N and sub_sum == K:
            cnt += 1
    return cnt



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 원소개수, S 는 총합
    arr = [i for i in range(1, 13)]
    print(f'#{tc} {sum_sub(arr, N, K)}')

'''



def sum_sub(arr, n, K): # arr에서 합계 구하기, K는 목표합계
    cnt = 0 # 10 만족하는 값 찾기
    for tar in range(0, 1<<n): # 모든 함수 반복
        sub_sum = 0
        subset = []
        for i in range(n):
            if tar & 0x1: # target과의 & 연산자가 True 인 경우
                sub_sum += arr[i]
                subset.append(arr[i])
            tar >>= 1
        # sub_sum과 목표합이 같으면 cnt
        if len(subset) == N and sub_sum == K:
            cnt += 1
    return cnt



T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split()) # N은 원소개수, S 는 총합
    arr = [i for i in range(1, 13)]
    n = len(arr)
    print(f'#{tc} {sum_sub(arr, N, K)}')
'''