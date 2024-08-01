'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''

T = int(input())

for tc in range(1, T+1):
    # N: 부분집합 원소 개수, K : 부분집합 원소의 합
    N, K = map(int, input().split())
    # 1~12까지의 숫자를 원소로 가진 집합 A
    arr = [i for i in range(1, 13)]
    # 정답 갯수
    result = 0
    for i in range(1 << 12): # 모든 부분집합 확인
        sum_sub = 0 # 부분집합의 합
        subset = [] # 부분 집합 리스트 초기화
        for j in range(12):
            if i & (1 << j): #j 번째 요소가 있는지 여부확인
                sum_sub += arr[j]
                subset.append(arr[j])

        if len(subset) == N and sum_sub == K:
            result += 1
    print(f'#{tc} {result}')




'''
import itertools
lst = [1, 2, 3]

# lst의 순열
ans1 = list(itertools.permutations((lst)))
# lst에서 N개의 원소를 가진 모든 조합(원소의 중복 없음
ans2 = list(itertools.combinations(lst, 2))
'''



'''
# 1. 조합 사용
import itertools

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    lst_comb = itertools.combinations(lst, N) # 리스트에서 N개의 원소를 가진 조합
    
    cnt = 0
    for i in lst_comb:
        if sum(i) == K: # 각 부분집합의 합 확인
            cnt += 1
    
    print(f'#{tc} {cnt}')
'''

''''''
# 2. 비트 연산 사용
# 1) 비트 이동 연산(<<)
# 1 << 3 --> 이진수 1을 왼쪽으로 3칸 밀기 --> 2진수 1000, 10진수 8
# 1000 의 3번째 비트가 1이다
# 2) 비트 AND 연산(&)
# 두 이진수의 각 자라를 비교하여, 둘 다 1이면 1, 그렇지 않으면 0
# ex) 1100 & 0101 == 0100


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    cnt = 0
    for i in range(1 << 12): # lst의 원소의 개수가 12개 => 부분집합의 갯수 4096개에 대해 순회
        sum_sub = 0 # 부분집합 원소의 합
        subset = [] # 현재 부분 집합
        for j in range(12): # 집합의 각 원소에 대해 반복
            if i & (1 << j): # i의 j번째 비트가 1인지 아닌지 판별
                sum_sub += lst[j] # 부분집합 합계 갱신
                subset.append(lst[j]) # 부분집합 케이스 추가
        if sum_sub == K and len(subset) == N:
            cnt += 1

# ex) i = 5 (== 이진수 0101
# j = 0 일때
# 0101 & 0001 --> True => 첫 번째 원소 포함
# j = 1일때
# 0101 & 0010 --> False => 두 번째 원소 포함X
# j = 2일때
# 0101 & 0100 --> True => 세 번째 원소 포함
# j = 3일때
# 0101 & 1000 --> False => 네 번째 원소 포함X

### [1, 3]이라는 부분집합 생성
#### 모든 부분집합 빠짐없이 생성 가능