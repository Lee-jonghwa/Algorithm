# selection sort

'''
def selection_sort(arr, N): # arr: 정렬대상, N: 크기(원소 개수)
    for i in range(N-1):    # 주어진 구간에 대한 기준위치 i를 정함
        min_idx = i         # 최소값 위치를 기준 위치로 가정
        for j in range(i+1, N):# 남은 원소에 대해 실제 최소값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 구간의 최소 위치로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]



A = [2, 7, 5, 3, 4, 123]
B = [4, 3, 2, 1]
selection_sort(A, len(A))
selection_sort(B, len(B))
print(A)
print(B)
'''
'''
def selections_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [51, 32, 56, 67, 86, 79, 99, 123, 33, 3, 2]
sorted_arr = selections_sort(arr)
print(sorted_arr)
'''

# 이진탐색

# 중간값 탐색

# 찾고자 하는 값과 비교 하여 양옆 탐색

def binary_searvch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start+end) // 2
        #타겟 찾으면 값 반환(인덱스)
        if arr[middle] == target:
            return middle
        # 타겟이 중간값 보다 클 때
        elif arr[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return -1


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]
target = 11
result = binary_searvch(arr, target)
print(f'target index : {result}')