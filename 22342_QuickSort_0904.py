
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # 피벗 선택
    pivot = arr[len(arr)//2]
    # 피벗보다 작으면 left
    left = [x for x in arr if x < pivot]
    # 피벗과 같으면 middle
    middle = [x for x in arr if x == pivot]
    # 피벗보다 크면 right
    right = [x for x in arr if x > pivot]

    # middle은 같으면 더이상 할 필요 없음
    return quick_sort(left) + middle + quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    result = quick_sort(arr)

    print(f'#{tc} {result[N//2]}')