'''
정렬 되어있는 데이터를 검색할 때,
for문으로 찾는 것보다 Binary Search로 더 빨리 원하는 값을 찾을 수 있습니다.
(Binary Search와 Binary Search Tree는 다릅니다.)

n개의 배열 값을 입력 받아주세요.
그리고 찾아야 하는 수를 입력 받고,
배열 내 존재하는 값인지 아닌지 O(log N) 속도로 찾는 프로그램을 작성해 주세요.

입력
첫 줄에는 수 n을 입력 받습니다. (1 <= n <= 100,000)
다음 줄에는 n개의 수가 입력으로 주어집니다. (n = Integer범위)
그리고 수 k가 입력됩니다. ( 1 <= n <= 1,000)
다음줄에는 k 개의 찾아야 하는 수가 입력됩니다.

출력
k개의 수가 배열 안에 존재하는지출력하는 프로그램을 작성해주세요.
각 수마다, 존재한다면 "O"를, 존재하지 않다면 "X"를 출력합니다
'''

'''
n = int(input()) # 찾는 공간 갯수
k = list(map(int, input().split())) # 찾는 공간
target_n = int(input()) # 타겟 갯수
target_lst = list(map(int, input().split())) # 타겟

sort_k = sorted(k) # 공간 정렬

def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

result = []
for i in target_lst:
    if binarySearch(sort_k, n, i) == True:
        result.append("O")
    else:
        result.append("X")

print(*result, sep="")

'''

# 강사님 풀이
def binary_search(target):
    s, e = 0, N
    while s <= e:
        mid = (s + e) // 2
        if A[mid] > target:
            e = mid - 1
        elif A[mid] < target:
            s = mid + 1
        elif A[mid] == target:
            return True
    return False

N = int(input())
A = sorted(list(map(int, input().split())))
K = int(input())
B = list(map(int, input().split()))
for b in B:
    if binary_search(b):
        print('O', end="")
    else:
        print('X', end="")