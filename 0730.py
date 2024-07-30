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

'''


'''
# 카운팅 정렬: 각 숫자의 개수를 세어서 정수를 정렬하는 알고리즘
numbers = [1, 4, 1 , 2, 7, 5, 2]

def counting(arr):
    # arr의 최댓값 구하기
    # max_v = max(arr) # max 사용
    max_v = float('-inf') # 음의 무한대
    for num in arr:
        if num > max_v:
            max_v = num
    # 카운트 배열 초기화
    count = [0] * (max_v + 1)
    # 카운팅! 각 숫자의 출현 횟수 세기
    for num in arr:
        count[num] += 1
    # 카운트 배열을 기반으로 정렬된 리스트 만들기
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]): # 해당 숫자가 몇 개 있는지
            sorted_arr.append(i) # 예 : 1이 2개일 경우 -> 1을 2번 append

    return sorted_arr

result = counting(numbers)
print(result)
'''

# 순열: 주어진 항목들로 만들 수 있는 모든 가능한 순서
# 중복순열: 중복을 허용한 순열
'''
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1: # 중복 방지
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2: # 중복 방지
                    print(i1, i2, i3)
'''

'''
# 순열 만드는 메서드
import itertools
lst = [1, 2, 3]
# permutations(lst) : lst의 순열(원소의 중복 O)
print(list(itertools.permutations(lst)))
# combinations(lst, N) : lst에서 N개의 원소를 가진 모든 조합(원소의 중복 X)
print(list(itertools.combinations(lst, 2)))
'''

# Greedy : 각 단계에서 가장 최선의 선택을 하는 방법
# 대표 예제 : 거스름돈(100원, 50원, 10원)
# 문제) 주어야 할 거스름 돈 380원, 동전 갯수 100, 50, 10
# Q) 가장 적은 수의 동전으로 거스름돈 주기
# A) {100: 3, 50: 1, 10:3}
# 거스름돈 줄 때 최선 : 큰 -> 작

# 100원: coin_h, 50원: coin_f, 10원: coin_t
# 총 지불금 pay_m

def greedy(money, coins):
    coins.sort(reverse=True) # 내림차순 정렬
    #거스름돈의 개수를 저장할 딕셔너리
    change = {coin: 0 for coin in coins} # 동전의 유형을 키로 만드는 딕셔너리 생성
    for coin in coins:
        while money >= coin: # 거슬러 줄 수 있는 동안 반복
            money -= coin # 현재 거스름돈에서 동전의 가치만큼 차감
            change[coin] += 1 # 해당 동전의 개수 증가
    return change

ans = greedy(380, [100, 50, 10])
print(ans)