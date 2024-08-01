'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.

10 1 9 2 8 3 7 4 6 5
주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    sort_lst = sorted(A)
    lst = [0] * 10
    for i in range(5):
            lst[2*i+1] = sort_lst[i]
            lst[2*i] = sort_lst[-i-1]
    print(f'#{tc}', *lst)
    # 가장큰수, 가장작은수, 두번째큰, 두번째 작은

#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21 69 26 64 30 62 36 60 43 59 46


'''
# 강사님풀이

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = []
    
    while len(nums) > 0:
        max_v = max(nums)
        nums.remove(max_v)
        result.append(max_v)
        
        min_v = min(nums)
        nums.remove(min_v)
        result.append(min_v)
    print(f'#{tc}', *result[:10])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    result = []
    lst_front, lst_back = [], []
    
    for i in range(len(nums)):
        if i < (len(nums) // 2):
            lst_front.append(nums[i])
        elif i > (len(nums) // 2) - 1:
            lst_back.append(nums[i])
    
    lst_back.sort(reverse=True)
    for i in range(5):
        result.append(lst_back[i])
        result.append(lst_front[i])
    print(f'#{tc}', *result)
'''