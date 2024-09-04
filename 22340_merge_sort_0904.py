
# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 => 가운데 분할
def merge_sort(arr):
    global cnt

    if len(arr) == 1:
        return arr

    # 배열 반으로 나누기
    mid = len(arr)//2
    # 왼쪽 절반 정렬
    left = merge_sort(arr[:mid])
    # 오른쪽 절반 정렬
    right = merge_sort(arr[mid:])
    # 정렬된 오른쪽과 왼쪽 넣기
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)


# 한 번 병합하는 정렬
def merge(left, right):
    global cnt
    result = [0]*(len(left) + len(right))
    i = j = 0

    # 왼쪽 오른쪽 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 왼쪽 요소가 작거나 같다
            result[i+j] = left[i]
            i += 1
        else:  # 오른쪽 요소가 더 작으면
            result[i+j] = right[j]
            j += 1

    # 남은 요소 넣기
    while i < len(left):
        result[i+j] = left[i]
        i += 1

    while j < len(right):
        result[i+j] = right[j]
        j += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    cnt = 0

    result = merge_sort(arr)

    print(f'#{tc} {result[N//2]} {cnt}')