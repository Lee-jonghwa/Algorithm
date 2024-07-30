
'''
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
'''

# 버블 정렬

'''
[63, 31, 27, 11, 25]
[31, 63, 27, 11, 25]
[31, 27, 63, 11, 25]
[31, 27, 11, 63, 25]
[31, 27, 11, 25, 63]
'''



# 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정 반복

numbers = [63, 31, 27, 11, 25]

def bubble(arr):
    # 배열의 모든 요소 순회
    for i in range(len(arr)):
        # 배열의 끝에서 정렬된 부분을 제외하고 순회
        # (가장 높은 게 마지막으로 가면, 다음으로 높은 게 감)
        for j in range(len(arr) - i - 1):
            # 인접한 두 요소 위치 바꾸기
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble(numbers)
print(numbers)

# debugger -> 함수 안으로 -> stepover -> 오류 검토