"""

## merge sort

def merge(left, right):
    result = []
    i, j = 0  # idx(i: left, j: right)

    # 왼쪽과 오른쪽 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 왼쪽 요소가 작거나 같다
            result.append(left[i])
            i += 1
        else:  # 오른쪽 요소가 더 작으면
            result.append(right[j])
            j += 1

    # 남은 거 다 넣기
    result.extend(left[i:])
    result.extend(right[i:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # 배열을 반으로 나누기
    mid = len(arr) // 2
    # 왼쪽 절반 정렬
    left = merge_sort(arr[:mid])
    # 오른쪽 절반 정렬
    right = merge_sort(arr[mid:])

    # 정렬된 오른쪽과 왼쪽 정렬
    return merge(left, right)

arr = list(map(int,input().split()))
sorted_arr = merge_sort(arr)

print(sorted_arr)

"""


"""

### Quick sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택: 가운데 요소
    pivot = arr[len(arr) // 2]
    # 피벗보다 작은 요소 left
    left = [x for x in arr if x < pivot]
    # 피벗과 같으면 middle
    middle = [x for x in arr if x == pivot]
    # 피벗보다 큰 요소는 right
    right = [x for x in arr if x > pivot]
    
    
    # 실행한 전체 병합
    return quick_sort(left) + middle + quick_sort(right)


arr = list(map(int, input().split()))
sorted_arr = quick_sort(arr)

print(sorted_arr)
"""


### binary search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 찾은 위치 반환
        elif arr[mid] < target:
            left = mid + 1 # 오른쪽 절반 탐색
        else:
            right = mid - 1

    return -1