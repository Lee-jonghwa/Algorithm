def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    # 오른쪽이면 1, 아니면 0
    is_right = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            # mid에 위치하면 정답임
            return True
        elif arr[mid] < key:
            # 오른쪽 - 오른쪽이면
            if is_right == 1:
                return False
            left = mid + 1  # 오른쪽 절반 탐색
            is_right = 1
        else:
            if is_right == 0:
                return False
            right = mid - 1
            is_right = 0

    return False


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    keys = list(map(int,input().split()))
    arr.sort()

    cnt = 0
    for key in keys:
        if binary_search(arr,key):
            cnt += 1

    print(f'#{tc} {cnt}')
